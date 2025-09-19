# Crop Recommendation (Flask)

This project trains a classifier on the Crop Recommendation dataset and serves a simple Flask web app to predict the best crop based on soil and weather parameters, similar to the referenced project.

- Reference repo: [Chando0185/Crop_Recommendation](https://github.com/Chando0185/Crop_Recommendation)
- Dataset: Kaggle "Crop Recommendation" (download `Crop_recommendation.csv`)

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Data

Place the Kaggle CSV at:

```
/Users/nikhilpradipmore/crop detection/data/Crop_recommendation.csv
```

Or pass a custom path to the training script.

## Train

```bash
python train.py --csv "/Users/nikhilpradipmore/crop detection/data/Crop_recommendation.csv"
```

Artifacts will be saved to `artifacts/model.pkl` and `artifacts/scaler.pkl`.

## Run the app

```bash
python app.py
```

Open `http://localhost:5000`.

## Notes

- Features: N, P, K, temperature, humidity, ph, rainfall
- Model: RandomForest + StandardScaler
- Inference scales inputs with the saved scaler, then predicts with the trained model
