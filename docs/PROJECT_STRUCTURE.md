# Project Structure

This project is organized around four main responsibilities.

## UI

Tkinter screens live in `app/ui`.

- `home_view.py`: landing screen
- `login_view.py`: login screen
- `register_view.py`: user registration
- `dashboard_view.py`: image upload and prediction dashboard
- `about_view.py`: team and system information
- `theme.py`: shared colors and simple styling helpers

## Machine Learning

ML code lives in `app/ml`.

- `prediction.py`: loads the model and runs prediction
- `preprocessing.py`: validates and prepares images for the model
- `smallervggnet.py`: model architecture used by training
- `train.py`: training script

## Data

Database code lives in `app/data`.

- `database.py`: SQLite setup, login, and registration helpers
- `Form1.db`: seed database copied into user app data at runtime

## Utilities

Shared helpers live in `app/utils`.

- `paths.py`: safe paths for development and packaged EXE mode
- `navigation.py`: screen navigation without relying on external Python files
