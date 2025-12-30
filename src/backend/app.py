# app.py
# Flask backend for climate visibility prediction

from flask import Flask, request, jsonify, render_template
import joblib
import os
from datetime import datetime   # ✅ FIX 1: import added

from weather_service import get_weather_data
from risk_logic import get_risk_and_advisory

# Create Flask app
app = Flask(__name__)

# Base project path
BASE_PATH = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))

# Frontend paths
app.template_folder = os.path.join(BASE_PATH, "src", "frontend", "templates")
app.static_folder = os.path.join(BASE_PATH, "src", "frontend", "static")

# Load trained ML model
MODEL_PATH = os.path.join(BASE_PATH, "models", "visibility_model.pkl")
model = joblib.load(MODEL_PATH)


# Home route (UI)
@app.route("/")
def home():
    return render_template("index.html")


# Prediction API
@app.route("/predict", methods=["POST"])
def predict_visibility():
    data = request.json

    time_window = data.get("time_window")
    lat = data.get("latitude")
    lon = data.get("longitude")
    location_name = data.get("location_name")

    # Build query for weather API
    if location_name:
        query = f"{location_name}, India"
        coordinates = "Manual location"
    else:
        query = f"{lat},{lon}"
        coordinates = f"Lat {round(lat, 4)}, Lon {round(lon, 4)}"

    # Fetch weather data based on selected time window
    weather = get_weather_data(query, time_window)

    if weather is None:
        return jsonify({
            "error": "Unable to fetch weather data for the given location"
        }), 400

    # Prepare ML input
    X = [[
        weather["temperature"],
        weather["humidity"],
        weather["wind_speed"],
        weather["rainfall"]
    ]]

    # Predict visibility
    predicted_visibility = round(float(model.predict(X)[0]), 2)

    # Risk level and advisory
    risk, advisory = get_risk_and_advisory(predicted_visibility)

    # Final response
    response = {
        "location": f"{weather['city']}, {weather['region']}, {weather['country']}",
        "coordinates": coordinates,
        "prediction_time": time_window,
        "last_updated": datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
        "predicted_visibility_km": predicted_visibility,
        "risk_level": risk,
        "advisory": advisory
    }

    return jsonify(response)


if __name__ == "__main__":
    # ✅ FIX 2: allow mobile devices on same network
    app.run(host="0.0.0.0", port=5000, debug=True)
