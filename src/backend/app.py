# app.py
# Flask backend for climate visibility prediction (Inference Only)

from flask import Flask, request, jsonify, render_template
import joblib
import os
from datetime import datetime

from src.backend.weather_service import get_weather_data
from src.backend.risk_logic import get_risk_and_advisory

# Create Flask app
app = Flask(__name__)

# Base project path
BASE_PATH = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))

# Frontend paths
app.template_folder = os.path.join(BASE_PATH, "src", "frontend", "templates")
app.static_folder = os.path.join(BASE_PATH, "src", "frontend", "static")

# Model path (pre-trained, inference only)
MODEL_PATH = os.path.join(BASE_PATH, "models", "visibility_model.pkl")

# Load pre-trained model
if not os.path.exists(MODEL_PATH):
    raise RuntimeError(
        "Pre-trained model not found. Train the model locally and place it in /models."
    )

model = joblib.load(MODEL_PATH)
print("Model loaded successfully (inference mode).")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict_visibility():
    data = request.json

    time_window = data.get("time_window")
    lat = data.get("latitude")
    lon = data.get("longitude")
    location_name = data.get("location_name")

    # Build query
    if location_name:
        query = f"{location_name}, India"
        coordinates = "Manual location"
    else:
        query = f"{lat},{lon}"
        coordinates = f"Lat {round(lat,4)}, Lon {round(lon,4)}"

    # Fetch live weather
    weather = get_weather_data(query, time_window)
    if weather is None:
        return jsonify({"error": "Weather data unavailable"}), 400

    # ML input
    X = [[
        weather["temperature"],
        weather["humidity"],
        weather["wind_speed"],
        weather["rainfall"]
    ]]

    predicted_visibility = round(float(model.predict(X)[0]), 2)
    risk, advisory = get_risk_and_advisory(predicted_visibility)

    return jsonify({
        "location": f"{weather['city']}, {weather['region']}, {weather['country']}",
        "coordinates": coordinates,
        "prediction_time": time_window,
        "last_updated": datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
        "predicted_visibility_km": predicted_visibility,
        "risk_level": risk,
        "advisory": advisory
    })


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
