from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.models import load_model
import numpy as np
import pickle
import cv2
import os

# Load model and label bin only once (IMPORTANT for performance)
print("[INFO] loading network...")
model = load_model("hrmodel.model")
lb = pickle.loads(open("lb.pickle", "rb").read())


def predict_personality(image_path):

    image = cv2.imread(image_path)
    image = cv2.resize(image, (96, 96))
    image = image.astype("float") / 255.0
    image = img_to_array(image)
    image = np.expand_dims(image, axis=0)

    print("[INFO] classifying image...")
    proba = model.predict(image)[0]
    idx = np.argmax(proba)

    label = lb.classes_[idx]
    confidence = float(proba[idx] * 100)

    return label, confidence
