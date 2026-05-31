import numpy as np
from pathlib import Path
from PIL import Image

from app.config import SUPPORTED_IMAGE_EXTENSIONS


IMAGE_DIMS = (96, 96)


class PreprocessingError(Exception):
    pass


def _load_cv2():
    try:
        import cv2
    except ImportError:
        return None

    return cv2


def validate_image_path(image_path):
    path = Path(image_path)

    if not path.exists():
        raise PreprocessingError(f"Image file was not found: {path}")

    if path.suffix.lower() not in SUPPORTED_IMAGE_EXTENSIONS:
        allowed = ", ".join(SUPPORTED_IMAGE_EXTENSIONS)
        raise PreprocessingError(f"Unsupported image type. Use: {allowed}")

    return path


def load_image(image_path):
    path = validate_image_path(image_path)
    cv2 = _load_cv2()

    if cv2 is not None:
        image = cv2.imread(str(path))

        if image is None:
            raise PreprocessingError("The selected file could not be read as an image.")

        return image

    try:
        with Image.open(path) as image:
            return np.asarray(image.convert("RGB"))
    except Exception as exc:
        raise PreprocessingError(
            "The selected file could not be read as an image."
        ) from exc


def resize_for_model(image):
    cv2 = _load_cv2()

    if cv2 is not None:
        return cv2.resize(image, IMAGE_DIMS)

    pil_image = Image.fromarray(image.astype("uint8"))
    pil_image = pil_image.resize(IMAGE_DIMS, Image.LANCZOS)
    return np.asarray(pil_image)


def normalize_image(image):
    return image.astype("float32") / 255.0


def preprocess_image(image_path):
    image = load_image(image_path)
    image = resize_for_model(image)
    image = normalize_image(image)
    image = np.expand_dims(image, axis=0)

    return image
