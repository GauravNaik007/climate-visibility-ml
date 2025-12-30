# train_model.py
# This file trains a Random Forest model to predict visibility
# The model is trained using the complete processed dataset

import pandas as pd
import os
import joblib

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score


def load_processed_data():
    base_path = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    data_path = os.path.join(
        base_path, "data", "processed", "processed_climate_data.csv"
    )

    print("Loading processed dataset...")
    df = pd.read_csv(data_path)
    print("Total records available:", len(df))

    return df


def prepare_data(df):
    """
    Select input features and target variable
    """
    X = df[["temperature", "humidity", "wind_speed", "rainfall"]]
    y = df["visibility"]

    print("Using full dataset for training:", len(df), "records")

    return X, y


def train_model(X, y):
    """
    Train Random Forest Regressor
    """
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    print("Training Random Forest model...")

    model = RandomForestRegressor(
        n_estimators=100,
        random_state=42,
        n_jobs=-1
    )

    model.fit(X_train, y_train)

    return model, X_test, y_test


def evaluate_model(model, X_test, y_test):
    """
    Evaluate model performance
    """
    predictions = model.predict(X_test)

    mae = mean_absolute_error(y_test, predictions)
    r2 = r2_score(y_test, predictions)

    print("\nModel Evaluation Results:")
    print("Mean Absolute Error (MAE):", round(mae, 2))
    print("R2 Score:", round(r2, 3))


def save_model(model):
    """
    Save trained model as .pkl file
    """
    base_path = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    model_dir = os.path.join(base_path, "models")

    if not os.path.exists(model_dir):
        os.makedirs(model_dir)

    model_path = os.path.join(model_dir, "visibility_model.pkl")
    joblib.dump(model, model_path)

    print("\nModel saved successfully at:")
    print(model_path)


if __name__ == "__main__":
    df = load_processed_data()
    X, y = prepare_data(df)

    model, X_test, y_test = train_model(X, y)
    evaluate_model(model, X_test, y_test)

    save_model(model)
