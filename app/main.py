from fastapi import FastAPI
from pydantic import BaseModel
from app.services.weather_api import fetch_rainfall_data
# import joblib

app = FastAPI(title="Landslide Early Warning API")

class CoordinateRequest(BaseModel):
    latitude: float
    longitude: float

@app.get("/")
def read_root():
    return {"status": "Active", "service": "Landslide Risk Fusion Engine"}

@app.post("/predict-risk")
def predict_risk(location: CoordinateRequest):
    weather = fetch_rainfall_data(location.latitude, location.longitude)
    
    # Placeholder for XGBoost ML Model Prediction (until model is trained)
    spatial_risk = 0.65  
    
    # Fusion Logic: Combine spatial ML risk with dynamic weather
    rainfall_factor = (weather["rainfall_24h"] * 0.6) + (weather["rainfall_7d"] * 0.4)
    
    if rainfall_factor > 150 and spatial_risk > 0.5:
        alert_level = "HIGH RISK - EVACUATION WARNING"
        risk_score = min(spatial_risk + 0.3, 1.0)
    elif rainfall_factor > 80 and spatial_risk > 0.4:
        alert_level = "MODERATE RISK - MONITORING REQUIRED"
        risk_score = spatial_risk + 0.1
    else:
        alert_level = "LOW RISK - SAFE"
        risk_score = spatial_risk

    return {
        "location": {"lat": location.latitude, "lon": location.longitude},
        "xgb_susceptibility_score": spatial_risk,
        "current_weather": weather,
        "fused_risk_score": round(risk_score, 3),
        "alert_status": alert_level
    }