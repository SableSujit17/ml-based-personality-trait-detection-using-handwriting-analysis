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

![Home screen](https://drive.google.com/file/d/1KRQfKoM_OEvMBSOl9HMd0H-18uRfi6yP/view)

### Registration Screen

![Registration screen](https://drive.google.com/file/d/1xZvhfNvmG4_X-TQGeuJ069y9C-hk76EK/viewg)

### Login Screen

![Login screen](https://drive.google.com/file/d/1J_zkqEoPrhafWTe7gcVNNordZ3kpyJp0/view)

### Upload Preview

![Upload preview](https://drive.google.com/file/d/1dy4IvxsLPfNJAuh5CAmqpvCP1rnW0uG0/view)

### Analysis Result

![Analysis result](https://drive.google.com/file/d/1XWvU3GmJA5xC_1E-S74np3X809tFsaeq/view)

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
