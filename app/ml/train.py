import argparse
import os
import pickle
import random


EPOCHS = 100
INIT_LR = 1e-3
BS = 32
IMAGE_DIMS = (96, 96, 3)


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-d",
        "--dataset",
        required=True,
        help="path to input dataset directory",
    )
    parser.add_argument(
        "-m",
        "--model",
        required=True,
        help="path to output model",
    )
    parser.add_argument(
        "-l",
        "--labelbin",
        required=True,
        help="path to output label binarizer",
    )
    parser.add_argument(
        "-p",
        "--plot",
        type=str,
        default="plot.png",
        help="path to output accuracy/loss plot",
    )
    return vars(parser.parse_args())


def main():
    from imutils import paths
    from sklearn.model_selection import train_test_split
    from sklearn.preprocessing import LabelBinarizer
    from tensorflow.keras.optimizers import Adam
    from tensorflow.keras.preprocessing.image import ImageDataGenerator
    import cv2
    import matplotlib

    matplotlib.use("Agg")

    import matplotlib.pyplot as plt
    import numpy as np

    from app.ml.smallervggnet import SmallerVGGNet

    args = parse_args()
    data = []
    labels = []

    print("[INFO] loading images...")
    image_paths = sorted(list(paths.list_images(args["dataset"])))

    random.seed(42)
    random.shuffle(image_paths)

    for image_path in image_paths:
        image = cv2.imread(image_path)

        if image is None:
            print(f"[WARN] skipping unreadable image: {image_path}")
            continue

        image = cv2.resize(image, (IMAGE_DIMS[1], IMAGE_DIMS[0]))
        data.append(image)
        labels.append(image_path.split(os.path.sep)[-2])

    if not data:
        raise RuntimeError("No readable training images were found.")

    data = np.array(data, dtype="float32") / 255.0
    labels = np.array(labels)

    print("[INFO] data matrix: {:.2f}MB".format(data.nbytes / (1024 * 1000.0)))

    lb = LabelBinarizer()
    labels = lb.fit_transform(labels)

    train_x, test_x, train_y, test_y = train_test_split(
        data,
        labels,
        test_size=0.2,
        random_state=42,
    )

    aug = ImageDataGenerator(
        rotation_range=25,
        width_shift_range=0.1,
        height_shift_range=0.1,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True,
        fill_mode="nearest",
    )

    print("[INFO] compiling model...")
    model = SmallerVGGNet.build(
        width=IMAGE_DIMS[1],
        height=IMAGE_DIMS[0],
        depth=IMAGE_DIMS[2],
        classes=len(lb.classes_),
    )
    opt = Adam(learning_rate=INIT_LR)
    model.compile(
        loss="categorical_crossentropy",
        optimizer=opt,
        metrics=["accuracy"],
    )

    print("[INFO] training network...")
    history = model.fit(
        aug.flow(train_x, train_y, batch_size=BS),
        validation_data=(test_x, test_y),
        steps_per_epoch=max(1, len(train_x) // BS),
        epochs=EPOCHS,
        verbose=1,
    )

    print("[INFO] serializing network...")
    model.save(args["model"])

    print("[INFO] serializing label binarizer...")
    with open(args["labelbin"], "wb") as file:
        pickle.dump(lb, file)

    plot_history(history.history, args["plot"], plt, np)


def plot_history(history, plot_path, plt, np):
    plt.style.use("ggplot")
    plt.figure()

    epochs = len(history.get("loss", []))
    x_axis = np.arange(0, epochs)

    if "loss" in history:
        plt.plot(x_axis, history["loss"], label="train_loss")

    if "val_loss" in history:
        plt.plot(x_axis, history["val_loss"], label="val_loss")

    accuracy_key = "accuracy" if "accuracy" in history else "acc"
    val_accuracy_key = "val_accuracy" if "val_accuracy" in history else "val_acc"

    if accuracy_key in history:
        plt.plot(x_axis, history[accuracy_key], label="train_acc")

    if val_accuracy_key in history:
        plt.plot(x_axis, history[val_accuracy_key], label="val_acc")

    plt.title("Training Loss and Accuracy")
    plt.xlabel("Epoch #")
    plt.ylabel("Loss/Accuracy")
    plt.legend(loc="upper left")
    plt.savefig(plot_path)


if __name__ == "__main__":
    main()
