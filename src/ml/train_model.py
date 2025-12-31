# train_model.py
# Trains ML model for climate visibility prediction

import os
import joblib
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split

# Base project path
BASE_PATH = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))

# Paths
DATA_PATH = os.path.join(BASE_PATH, "data", "processed", "processed_climate_data.csv")
MODEL_DIR = os.path.join(BASE_PATH, "models")
MODEL_PATH = os.path.join(MODEL_DIR, "visibility_model.pkl")


def train_and_save_model():
    print("Starting model training...")

    # Load dataset
    df = pd.read_csv(DATA_PATH)

    # Select features and target
    X = df[["temperature", "humidity", "wind_speed", "rainfall"]]
    y = df["visibility"]

    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # Train model
    model = RandomForestRegressor(
        n_estimators=100,
        random_state=42,
        n_jobs=-1
    )
    model.fit(X_train, y_train)

    # Ensure model directory exists
    os.makedirs(MODEL_DIR, exist_ok=True)

    # Save model
    joblib.dump(model, MODEL_PATH)

    print("Model trained and saved successfully.")

    return model


# Allow manual training (optional)
if __name__ == "__main__":
    train_and_save_model()
