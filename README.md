# 🌾 Crop Recommendation System

![Python](https://img.shields.io/badge/Python-3.8+-blue?style=for-the-badge&logo=python)
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![ML](https://img.shields.io/badge/Machine%20Learning-green?style=for-the-badge)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn)
![Status](https://img.shields.io/badge/Status-Complete-brightgreen?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)

> An intelligent crop recommendation system that suggests the most suitable crop to plant based on soil properties (NPK values), temperature, humidity, pH, and rainfall — helping farmers maximize yield and optimize resources.

---

## 📌 Project Overview

Choosing the right crop for specific soil and weather conditions is critical for maximizing agricultural productivity. This project builds a **Crop Recommendation System** using machine learning to predict the best crop to plant based on environmental and soil parameters.

The system is deployed as a **Flask web application** with a clean HTML interface, allowing farmers to input their field conditions and instantly receive crop recommendations.

---

## 🎯 Key Highlights

- ✅ Recommends optimal crop based on **7 key parameters**
- ✅ Trained on real agricultural dataset with multiple crop types
- ✅ **Flask web app** with user-friendly HTML interface
- ✅ Saved **model.pkl** and **scaler.pkl** for instant predictions
- ✅ Production-ready deployment with `requirements.txt`

---

## 📊 Input Parameters

The system takes **7 environmental and soil features** as input:

| Feature | Description | Unit |
|---|---|---|
| **N** | Nitrogen content in soil | ratio |
| **P** | Phosphorus content in soil | ratio |
| **K** | Potassium content in soil | ratio |
| **Temperature** | Average temperature | °C |
| **Humidity** | Relative humidity | % |
| **pH** | Soil pH level | 0-14 scale |
| **Rainfall** | Average rainfall | mm |

---

## 🌱 Recommended Crops

The system can recommend from multiple crop types including:

**Common crops:**
- Rice, Wheat, Maize
- Cotton, Jute
- Chickpea, Lentil, Kidney Beans
- Mung Bean, Black Gram, Pigeon Peas
- Coffee, Orange, Banana, Mango, Grapes, Watermelon
- Coconut, Papaya, Apple

---

## 🧠 How It Works

### 1. Data Collection
- Dataset: `Crop_recommendation.csv` with soil and weather parameters
- Multiple crop types labeled with ideal growing conditions

### 2. Model Training (`train.py`)
- Features are normalized using **StandardScaler**
- Machine learning classifier trained on agricultural data
- Model saved as `model.pkl`, scaler saved as `scaler.pkl`

### 3. Web Application (`app.py`)
- **Flask backend** loads the trained model
- User inputs soil/weather parameters via HTML form
- Model predicts the best crop
- Results displayed on `result.html`

---

## 🛠️ Tech Stack

| Tool | Purpose |
|---|---|
| Python | Core programming language |
| Scikit-learn | ML model training & prediction |
| Flask | Web framework |
| Pandas | Data preprocessing |
| NumPy | Numerical operations |
| HTML/CSS | Frontend interface |

---

## 🚀 How to Run

### 1. Clone the repository
```bash
git clone https://github.com/Khiladi-786/Crop-Detection.git
cd Crop-Detection
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the Flask app
```bash
python app.py
```

### 4. Open browser
```
http://localhost:5000
```

### 5. Enter your field parameters
- Fill in NPK values, temperature, humidity, pH, and rainfall
- Click **"Get Recommendation"**
- View the recommended crop!

---

## 📁 Project Structure

```
Crop-Detection/
│
├── app.py                      # Flask web application
├── train.py                    # Model training script
├── model.pkl                   # Trained ML model
├── scaler.pkl                  # Feature scaler
├── Crop_recommendation.csv     # Agricultural dataset
├── requirements.txt            # Python dependencies
│
├── index.html                  # Input form
├── result.html                 # Prediction results
└── style.css                   # Styling
```

---

## 💡 Example Use Case

**Farmer's Input:**
```
N (Nitrogen): 90
P (Phosphorus): 42
K (Potassium): 43
Temperature: 20.8°C
Humidity: 82%
pH: 6.5
Rainfall: 202 mm
```

**System Output:**
```
🌾 Recommended Crop: RICE
```

**Why?** Rice thrives in high humidity, moderate temperature, and good rainfall — perfectly matching the input conditions.

---

## 🏆 Benefits for Farmers

- 📈 **Maximize Yield:** Plant the crop best suited to your soil
- 💰 **Optimize Resources:** Avoid planting crops that won't thrive
- 🌍 **Sustainable Farming:** Make data-driven decisions
- ⏱️ **Instant Results:** No need for trial and error

---

## 👨‍💻 About the Author

**Nikhil More**
B.Tech CSE (AI/ML) — University of Mumbai (2023–2027)

- 🔗 [LinkedIn](https://www.linkedin.com/in/nikhil-moretech)
- 🐙 [GitHub](https://github.com/Khiladi-786)
- 📧 morenikhil7822@gmail.com

*Using ML to solve real-world agricultural problems and support sustainable farming practices.*

---

## 📄 License

This project is licensed under the MIT License.

---

⭐ **If you found this project useful, please give it a star!**
