from functools import lru_cache
import logging
import numpy as np
import os
import pickle

from app.ml.preprocessing import PreprocessingError, preprocess_image
from app.utils.paths import fallback_user_data_dir, model_path, user_data_dir


logger = logging.getLogger(__name__)


class PredictionError(Exception):
    pass


DEFAULT_LABELS = np.array([
    "criminal_intent",
    "excitable",
    "honest",
    "narcissist",
    "persistent",
])


def load_label_classes(label_file):
    try:
        label_bin = pickle.loads(label_file.read_bytes())
        return np.asarray(label_bin.classes_)
    except ModuleNotFoundError as exc:
        logger.info(
            "Could not import label-binarizer dependency %s; using bundled label order.",
            exc.name,
        )
        return DEFAULT_LABELS
    except Exception as exc:
        raise PredictionError(f"Could not load label file: {exc}") from exc


def configure_ml_environment():
    os.environ.setdefault("TF_CPP_MIN_LOG_LEVEL", "2")

    try:
        mpl_config_dir = user_data_dir() / "matplotlib"
        mpl_config_dir.mkdir(parents=True, exist_ok=True)
    except OSError:
        mpl_config_dir = fallback_user_data_dir() / "matplotlib"
        mpl_config_dir.mkdir(parents=True, exist_ok=True)

    os.environ.setdefault("MPLCONFIGDIR", str(mpl_config_dir))


def load_legacy_hdf5_model(model_file, classes):
    import h5py
    from tensorflow.keras import backend as K

    from app.ml.smallervggnet import SmallerVGGNet

    K.clear_session()
    model = SmallerVGGNet.build(
        width=96,
        height=96,
        depth=3,
        classes=len(classes),
        legacy_names=True,
    )

    with h5py.File(model_file, "r") as file:
        if "model_weights" not in file:
            raise PredictionError("Legacy model file does not contain model weights.")

        model_weights = file["model_weights"]

        for layer in model.layers:
            if layer.name not in model_weights:
                continue

            layer_group = model_weights[layer.name]
            weight_names = layer_group.attrs.get("weight_names", [])

            if len(weight_names) == 0:
                continue

            weights = []

            for weight_name in weight_names:
                if isinstance(weight_name, bytes):
                    weight_name = weight_name.decode("utf-8")

                dataset = layer_group

                for path_part in weight_name.split("/"):
                    dataset = dataset[path_part]

                weights.append(dataset[()])

            layer.set_weights(weights)

    return model


@lru_cache(maxsize=1)
def load_prediction_assets():
    model_file = model_path("hrmodel.model")
    label_file = model_path("lb.pickle")

    if not model_file.exists():
        raise PredictionError(f"Model file was not found: {model_file}")

    if not label_file.exists():
        raise PredictionError(f"Label file was not found: {label_file}")

    configure_ml_environment()
    classes = load_label_classes(label_file)

    try:
        from tensorflow.keras.models import load_model
    except ImportError as exc:
        raise PredictionError(
            "TensorFlow is not installed. Install the packages from requirements.txt "
            "before running handwriting prediction."
        ) from exc

    logger.info("Loading prediction model")
    try:
        model = load_model(str(model_file), compile=False)
    except Exception as exc:
        logger.info("Falling back to legacy HDF5 weight loading: %s", exc)
        try:
            model = load_legacy_hdf5_model(model_file, classes)
        except Exception as fallback_exc:
            raise PredictionError(
                f"Could not load model file: {fallback_exc}"
            ) from fallback_exc

    return model, classes


def predict_personality(image_path):
    try:
        image = preprocess_image(image_path)
        model, classes = load_prediction_assets()
    except (PreprocessingError, PredictionError) as exc:
        logger.info("Prediction input failed: %s", exc)
        raise PredictionError(str(exc)) from exc

    try:
        proba = model.predict(image, verbose=0)[0]
    except Exception as exc:
        raise PredictionError(f"Model prediction failed: {exc}") from exc

    idx = np.argmax(proba)

    if idx >= len(classes):
        raise PredictionError(
            f"Model returned class index {idx}, but only {len(classes)} labels are available."
        )

    label = classes[idx]
    confidence = float(proba[idx] * 100)

    return label, confidence
