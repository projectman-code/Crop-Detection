from __future__ import annotations

import os
import argparse
import joblib
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.metrics import classification_report
from sklearn.ensemble import RandomForestClassifier

ARTIFACTS_DIR = os.path.join(os.path.dirname(__file__), "artifacts")
DEFAULT_DATA_PATH = os.path.join(os.path.dirname(__file__), "data", "Crop_recommendation.csv")


def ensure_dirs() -> None:
	os.makedirs(ARTIFACTS_DIR, exist_ok=True)


def load_data(csv_path: str) -> pd.DataFrame:
	if not os.path.exists(csv_path):
		raise FileNotFoundError(f"CSV not found at {csv_path}. Place the Kaggle dataset there.")
	return pd.read_csv(csv_path)


def train(csv_path: str) -> None:
	ensure_dirs()
	df = load_data(csv_path)

	feature_cols = ["N", "P", "K", "temperature", "humidity", "ph", "rainfall"]
	X = df[feature_cols]
	y = df["label"]

	X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

	model = Pipeline([
		("scaler", StandardScaler()),
		("clf", RandomForestClassifier(n_estimators=300, random_state=42))
	])

	model.fit(X_train, y_train)

	y_pred = model.predict(X_test)
	print(classification_report(y_test, y_pred))

	# Extract scaler for serving parity
	scaler: StandardScaler = model.named_steps["scaler"]
	clf: RandomForestClassifier = model.named_steps["clf"]

	joblib.dump(clf, os.path.join(ARTIFACTS_DIR, "model.pkl"))
	joblib.dump(scaler, os.path.join(ARTIFACTS_DIR, "scaler.pkl"))
	print(f"Saved artifacts to {ARTIFACTS_DIR}")


if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument("--csv", default=DEFAULT_DATA_PATH, help="Path to Crop_recommendation.csv")
	args = parser.parse_args()
	train(args.csv)
