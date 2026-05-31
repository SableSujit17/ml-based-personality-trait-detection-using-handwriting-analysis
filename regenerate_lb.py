from sklearn.preprocessing import LabelBinarizer
import pickle
from pathlib import Path

# Your personality classes
labels = [
    "criminal_intent",
    "excitable",
    "honest",
    "narcissist",
    "persistent"
]

lb = LabelBinarizer()
lb.fit(labels)

output_path = Path("models/lb.pickle")

with open(output_path, "wb") as f:
    pickle.dump(lb, f)

print("New lb.pickle generated successfully")