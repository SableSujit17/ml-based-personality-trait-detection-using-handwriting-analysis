import argparse
import sys

from app.ml.prediction import PredictionError, predict_personality


def main():
    parser = argparse.ArgumentParser(
        description="Classify a handwriting image with the bundled app model."
    )
    parser.add_argument(
        "-i",
        "--image",
        required=True,
        help="path to input handwriting image",
    )
    parser.add_argument(
        "-m",
        "--model",
        help="kept for compatibility; the app uses models/hrmodel.model",
    )
    parser.add_argument(
        "-l",
        "--labelbin",
        help="kept for compatibility; the app uses models/lb.pickle",
    )

    args = parser.parse_args()

    try:
        label, confidence = predict_personality(args.image)
    except PredictionError as exc:
        print(f"Prediction Error: {exc}", file=sys.stderr)
        return 1

    print(f"{label}: {confidence:.2f}%")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
