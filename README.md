# 🧠 Machine Learning Mastery — Educational & Career Platform

A comprehensive, interactive Machine Learning and Data Science educational portal featuring hands-on laboratories, real-time ML prediction models, FAANG system design case studies, interactive 3D visualizations, SQL mastery modules, and career preparation roadmaps.

---

## 🚀 Key Features

- **🏠 Real-World ML Predictor**: Live FastAPI-powered endpoint utilizing a trained Scikit-Learn regression model for real-time house price predictions.
- **🧊 Interactive 3D ML Lab**: Interactive visual simulations for machine learning concept exploration and decision boundary intuitions.
- **🐍 In-Browser Python WASM Sandbox**: Run and test Python ML scripts directly inside the browser using WebAssembly.
- **📊 SQL for Data Science**: Deep-dive modules, exercises, and real-world queries for data engineering and analysis.
- **🏛️ FAANG System Design & Case Studies**: End-to-end architectures of large-scale ML systems (recommendation engines, fraud detection, ranking).
- **⚡ Algorithm Arena & Quizzes**: Algorithm visualizers, flashcards, knowledge quizzes, and resume/certificate builders.
- **⚡ FastAPI High-Performance Backend**: Seamless static asset serving and RESTful prediction API.

---

## 📁 Project Structure

```text
├── ml_educational_platform/
│   ├── backend/
│   │   ├── main.py             # FastAPI backend server with static mounting & CORS
│   │   ├── model.pkl           # Serialized Scikit-Learn regression model
│   │   └── requirements.txt    # Python dependencies
│   ├── frontend/
│   │   ├── index.html          # Main platform portal
│   │   ├── full_platform.html  # Complete modules hub
│   │   ├── real_world_ml.html  # Interactive model prediction UI
│   │   ├── interactive_3d_lab.html
│   │   ├── python_sandbox_wasm.html
│   │   ├── sql_for_data_science.html
│   │   ├── algorithm_arena.html
│   │   ├── faang_system_case_studies.html
│   │   ├── style.css
│   │   └── script.js
│   └── ml_model/
│       └── train_model.py      # Dataset generation, training, and model export script
├── .gitignore
└── README.md
```

---

## 🛠️ Quick Start Guide

### 1. Prerequisites
Ensure you have **Python 3.10+** installed on your system.

### 2. Install Dependencies
```bash
cd ml_educational_platform/backend
pip install -r requirements.txt
```

### 3. (Optional) Train the Machine Learning Model
To regenerate or retrain the model weights:
```bash
python ../ml_model/train_model.py
```

### 4. Run the Server
Launch the FastAPI backend server:
```bash
uvicorn main:app --host 127.0.0.1 --port 8000 --reload
```

---

## 🌐 Endpoints & URLs

| Route | Description |
| :--- | :--- |
| **`http://localhost:8000/`** | Platform Main Dashboard & Portal |
| **`http://localhost:8000/real_world_ml.html`** | Interactive ML Model UI & Price Predictor |
| **`http://localhost:8000/interactive_3d_lab.html`** | 3D Interactive ML Visualizations |
| **`http://localhost:8000/python_sandbox_wasm.html`** | WebAssembly Python Sandbox |
| **`http://localhost:8000/sql_for_data_science.html`** | SQL for Data Science Course & Exercises |
| **`http://localhost:8000/docs`** | Swagger UI Interactive API Documentation |
| **`http://localhost:8000/api/predict`** | `POST` Endpoint for Model Predictions |

---

## 📦 API Example

### Predict House Price (`POST /api/predict`)

**Request Body:**
```json
{
  "sqft": 2200,
  "beds": 3
}
```

**Response:**
```json
{
  "estimated_price": 411836.73,
  "sqft": 2200.0,
  "beds": 3
}
```
