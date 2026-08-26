from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
import joblib
import os

# Initialize FastAPI app
app = FastAPI(title="House Price Predictor API")

# Allow requests from our frontend (CORS)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # For educational purposes, allow all. In prod, specify the domain.
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load the trained model when the API starts
# The model should be in the same directory as this main.py
MODEL_PATH = os.path.join(os.path.dirname(__file__), "model.pkl")

# We will load it safely in a startup event or globally if it exists
try:
    model = joblib.load(MODEL_PATH)
except Exception as e:
    model = None
    print(f"Warning: Could not load model from {MODEL_PATH}. Error: {e}")

# Define the structure of the incoming data
class HouseData(BaseModel):
    sqft: float
    beds: int

@app.get("/api/health")
def health_check():
    return {"status": "ok", "model_loaded": model is not None}

@app.post("/api/predict")
def predict_price(data: HouseData):
    if model is None:
        return {"error": "Model not loaded. Please train the model first."}
    
    # 1. Prepare data for the model (must be 2D array: [[sqft, beds]])
    input_features = [[data.sqft, data.beds]]
    
    # 2. Make prediction
    prediction = model.predict(input_features)[0]
    
    # 3. Return the result as JSON
    return {
        "estimated_price": round(prediction, 2),
        "sqft": data.sqft,
        "beds": data.beds
    }

# Mount static frontend directory to serve all HTML, CSS, and JS files seamlessly
FRONTEND_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "frontend"))
if os.path.exists(FRONTEND_DIR):
    app.mount("/", StaticFiles(directory=FRONTEND_DIR, html=True), name="frontend")
else:
    @app.get("/")
    def read_root():
        return {"message": "Welcome to the ML Educational API. Model is running!"}

