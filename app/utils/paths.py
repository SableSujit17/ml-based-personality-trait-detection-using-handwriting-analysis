import os
import sys
from pathlib import Path

from app.config import APP_DATA_FOLDER


def _resource_base():
    if hasattr(sys, "_MEIPASS"):
        return Path(sys._MEIPASS)

    return Path(__file__).resolve().parents[2]


BASE_DIR = _resource_base()
APP_DIR = BASE_DIR / "app"
ASSETS_DIR = BASE_DIR / "assets"
IMAGE_DIR = ASSETS_DIR / "images"
MODELS_DIR = BASE_DIR / "models"
SEED_DATA_DIR = APP_DIR / "data"


def image_path(filename):
    return IMAGE_DIR / filename


def model_path(filename):
    return MODELS_DIR / filename


def seed_data_path(filename):
    return SEED_DATA_DIR / filename


def user_data_dir():
    override = os.environ.get("HANDWRITING_APP_DATA_DIR")

    if override:
        folder = Path(override)
    else:
        local_app_data = os.environ.get("LOCALAPPDATA")
        if local_app_data:
            folder = Path(local_app_data) / APP_DATA_FOLDER
        else:
            folder = Path.home() / f".{APP_DATA_FOLDER}"

    folder.mkdir(parents=True, exist_ok=True)
    return folder


def fallback_user_data_dir():
    if hasattr(sys, "_MEIPASS"):
        base_dir = Path.cwd()
    else:
        base_dir = BASE_DIR

    folder = base_dir / "logs" / "runtime-data"
    folder.mkdir(parents=True, exist_ok=True)
    return folder


def data_path(filename):
    return user_data_dir() / filename


def fallback_data_path(filename):
    return fallback_user_data_dir() / filename
