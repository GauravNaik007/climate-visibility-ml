# data_preprocessing.py
# Preprocess raw climate data for ML training
# Only required columns are selected programmatically

import pandas as pd
import os


def load_raw_data():
    base_path = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    file_path = os.path.join(base_path, "data", "raw", "climate_data.csv")

    print("Loading raw dataset...")
    df = pd.read_csv(file_path)
    print("Raw dataset shape:", df.shape)

    return df


def preprocess_data(df):
    print("Starting preprocessing...")

    # Rename required columns to simple ML-friendly names
    df = df.rename(columns={
        "temperature_celsius": "temperature",
        "humidity": "humidity",
        "wind_kph": "wind_speed",
        "precip_mm": "rainfall",
        "visibility_km": "visibility"
    })

    # Select only required columns for ML
    df = df[[
        "temperature",
        "humidity",
        "wind_speed",
        "rainfall",
        "visibility"
    ]]

    # Drop rows with missing values
    df = df.dropna()

    print("Dataset shape after preprocessing:", df.shape)

    return df


def save_processed_data(df):
    base_path = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    output_dir = os.path.join(base_path, "data", "processed")

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    output_file = os.path.join(output_dir, "processed_climate_data.csv")
    df.to_csv(output_file, index=False)

    print("Processed dataset saved at:", output_file)


if __name__ == "__main__":
    raw_df = load_raw_data()
    clean_df = preprocess_data(raw_df)
    save_processed_data(clean_df)
