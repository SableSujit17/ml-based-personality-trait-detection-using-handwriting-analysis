# ml-based-personality-trait-detection-using-handwriting-analysis

A Tkinter-based desktop application that analyzes a handwriting image and predicts a personality trait using a trained TensorFlow/Keras model.

## Features

- Login and registration screens backed by SQLite
- Handwriting image upload from the local machine
- TensorFlow/Keras prediction using the bundled model
- Confidence percentage display
- About page with project/team details
- Windows packaging files for building an executable

## Screenshots

### Home Screen

![Home screen](docs/screenshots/home-screen.jpg)

### Registration Screen

![Registration screen](docs/screenshots/registration-screen.jpg)

### Login Screen

![Login screen](docs/screenshots/login-screen.jpg)

### Upload Preview

![Upload preview](docs/screenshots/upload-preview.jpg)

### Analysis Result

![Analysis result](docs/screenshots/analysis-result.jpg)

## Project Structure

```text
app/
  data/          SQLite seed database and database helpers
  ml/            prediction, preprocessing, training, and model architecture
  ui/            Tkinter screens and UI styling
  utils/         navigation and path helpers
assets/images/   UI images and profile images
models/          trained model and label binarizer
dataset/         training dataset
examples/        sample images
FINAL_DESKTOP_APP/
                 local generated desktop app output
installer/       installer notes
tests/           future tests
```

## Run The Desktop App

On this local machine, open:

```text
FINAL_DESKTOP_APP/Handwriting Personality Analyzer/Handwriting Personality Analyzer.exe
```

`FINAL_DESKTOP_APP` is generated output and is ignored in Git because the packaged TensorFlow desktop runtime is too large for a normal repository. To recreate it after cloning, run the build command below.

## Run In Development

Install dependencies first:

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

Then run:

```powershell
.\.venv\Scripts\python.exe home.py
```

You can also run the package entry point:

```powershell
.\.venv\Scripts\python.exe -m app
```

## Build Windows EXE

Install the dependencies first, then run:

```powershell
.\.venv\Scripts\python.exe -m PyInstaller --noconfirm --workpath build_final_app --distpath FINAL_DESKTOP_APP "Handwriting Personality Analyzer.spec"
```

The build uses PyInstaller and `Handwriting Personality Analyzer.spec`.

## Notes

- The app expects `models/hrmodel.model` and `models/lb.pickle` to exist.
- Runtime user data is stored under the user's local app data folder.
- For GitHub, consider Git LFS for large model or dataset files.
