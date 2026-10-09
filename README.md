# 🌍 AI-Based Landslide Early Warning System

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-green.svg)
![XGBoost](https://img.shields.io/badge/XGBoost-1.7+-red.svg)
![Google Earth Engine](https://img.shields.io/badge/Google%20Earth%20Engine-Geospatial-orange.svg)

An intelligent microservice architecture designed for landslide susceptibility assessment, monitoring, and early warning. This system fuses static geospatial ML predictions with dynamic weather data to generate real-time risk alerts.

## 🏗️ System Architecture

The project operates in three primary phases:

1. **Spatial Feature Extraction (Google Earth Engine):**
   - Uses historical landslide coordinates (NASA GLC/GSI).
   - Extracts topographic and environmental features (SRTM DEM for Elevation, Slope, Aspect, and Sentinel-2 for NDVI).
   - Exports the structured dataset for training.

2. **Susceptibility Modeling (XGBoost):**
   - Binary classification model trained on GEE features.
   - Outputs a calibrated spatial risk probability (0.0 to 1.0) for a given coordinate.

3. **Real-Time Fusion & Alerting (FastAPI Backend):**
   - Ingests dynamic 24-hour and 7-day antecedent rainfall data via weather APIs.
   - Computes Total Risk = `(XGBoost_Spatial_Risk) + (Dynamic_Rainfall_Trigger)`.
   - Generates early warning alerts if the risk exceeds defined safety thresholds.

## 🚀 Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/Devang-codeX/landslide-early-warning.git](https://github.com/Devang-codeX/landslide-early-warning.git)
   cd landslide-early-warning
   ```
