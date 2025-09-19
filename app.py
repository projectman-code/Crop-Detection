from __future__ import annotations

import os
import joblib
import numpy as np
from flask import Flask, render_template, request

app = Flask(__name__)

MODEL_PATH = os.path.join(os.path.dirname(__file__), "artifacts", "model.pkl")
SCALER_PATH = os.path.join(os.path.dirname(__file__), "artifacts", "scaler.pkl")

_model = None
_scaler = None


def load_artifacts() -> None:
	global _model, _scaler
	if _model is None and os.path.exists(MODEL_PATH):
		_model = joblib.load(MODEL_PATH)
	if _scaler is None and os.path.exists(SCALER_PATH):
		_scaler = joblib.load(SCALER_PATH)


@app.route("/")
def index():
	load_artifacts()
	return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
	load_artifacts()

	try:
		N = float(request.form.get("N", 0))
		P = float(request.form.get("P", 0))
		K = float(request.form.get("K", 0))
		temperature = float(request.form.get("temperature", 0))
		humidity = float(request.form.get("humidity", 0))
		ph = float(request.form.get("ph", 0))
		rainfall = float(request.form.get("rainfall", 0))
	except Exception:
		return render_template("result.html", prediction=None, error="Invalid input values.")

	features = np.array([[N, P, K, temperature, humidity, ph, rainfall]], dtype=float)

	if _scaler is not None:
		features = _scaler.transform(features)

	if _model is None:
		return render_template("result.html", prediction=None, error="Model not found. Please train the model first.")

	pred = _model.predict(features)[0]

	return render_template("result.html", prediction=str(pred), error=None)


if __name__ == "__main__":
	port = int(os.environ.get("PORT", 8080))
	app.run(host="0.0.0.0", port=port, debug=True)
