import random

def fetch_rainfall_data(lat: float, lon: float):
    """
    Mock weather API service for architecture demonstration. 
    In production, this will integrate with Open-Meteo or IMD APIs.
    """
    return {
        "rainfall_24h": round(random.uniform(0, 150), 2),
        "rainfall_7d": round(random.uniform(50, 400), 2)
    }