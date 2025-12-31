# Climate Visibility Prediction Using Machine Learning  
*(Agricultural Decision Support System)*

---

## 1. Introduction

Climate conditions such as fog and low visibility can directly affect agricultural
activities like spraying, harvesting, irrigation, and early-morning farm operations.
Sudden fog formation may cause crop damage, reduced efficiency, or safety risks.

This project predicts **climate visibility (fog risk)** using **machine learning**
and live weather data to help farmers make better decisions such as whether to
proceed with work, delay activities, or take precautions.

The system is designed as an **academic, real-time decision support prototype**
with a simple and explainable approach.

---

## 2. Problem Statement

Farmers often rely on personal experience or general weather reports to judge
visibility conditions. These methods may not always be accurate or location-specific.

There is a need for a system that:
- Uses real-time climate data
- Predicts visibility quantitatively (in kilometers)
- Provides clear, actionable advice
- Is easy to understand for non-technical users

---

## 3. Proposed Solution

This project uses a **machine learning regression model** trained on historical
climate data to predict visibility based on the following parameters:

- Temperature
- Humidity
- Wind Speed
- Rainfall

Live weather data is fetched using a weather API based on the user’s location
(GPS or manual input). The trained model then predicts visibility and categorizes
the risk level.

---

## 4. System Features

- Predicts visibility (in km) related to fog conditions
- Supports GPS-based and manual location input
- Uses live weather data for real-time prediction
- Provides risk level: **SAFE / MODERATE / HIGH**
- Displays advisory messages for farmers
- Web-based interface accessible on desktop and mobile
- Simple and explainable ML model (no deep learning)

---

## 5. Technology Stack

- **Programming Language:** Python  
- **Backend:** Flask  
- **Machine Learning:** Scikit-learn (Random Forest Regressor)  
- **Data Processing:** Pandas  
- **Frontend:** HTML, CSS, JavaScript  
- **API:** Live Weather API  

---

## 6. Machine Learning Approach

- **Algorithm Used:** Random Forest Regressor  
- **Reason for Selection:**
  - Handles non-linear relationships well
  - Robust to noise
  - Easy to explain compared to deep learning models

### Input Features:
- Temperature
- Humidity
- Wind Speed
- Rainfall

### Output:
- Predicted Visibility (km)
- Risk Level (SAFE / MODERATE / HIGH)
- Advisory Message

---

## 7. Dataset Description

The model is trained using a historical climate dataset stored in CSV format.
The dataset contains multiple climate-related parameters collected over time.

Only relevant columns are used for training:
- Temperature
- Humidity
- Wind Speed
- Rainfall
- Visibility

The dataset may contain a large number of records, ensuring better generalization.

---

## 8. Model Training Strategy

The machine learning model is trained **locally** using the training script provided
in the project. Training the model locally avoids cloud resource limitations and
follows standard industry practice.

Once trained, the model is saved as:
models/visibility_model.pkl


This trained model is then used for real-time prediction.

---

## 9. Why the Trained Model File Is Not Uploaded to GitHub

The trained model file (`visibility_model.pkl`) is intentionally **not included**
in this repository due to the following reasons:

- GitHub file size limitations
- Best practices in machine learning projects
- The model can be regenerated using the training script
- In real-world systems, models are often trained offline and deployed separately

This approach is academically and professionally accepted.

---

## 10. Real-Time Prediction Explanation

Although the model is pre-trained, the system still performs **real-time prediction**
because:

- Live weather data is fetched at request time
- Predictions are generated instantly using current conditions
- Advisory decisions are based on real-time inputs

The model does **not** need to be retrained for every prediction, which ensures
fast response and stable performance.

---

## 11. How to Run the Project (Local Demo)

### Step 1: Clone the Repository

git clone https://github.com/GauravNaik007/climate-visibility-ml.git
cd climate-visibility-ml

### Step 2: Install Dependencies
pip install -r requirements.txt

### Step 3: Train the Model
python src/ml/train_model.py

This will generate:
models/visibility_model.pkl

### Step 4: Run the Application
python -m src.backend.app


### Step 5: Open in Browser
http://127.0.0.1:5000

The application can also be accessed on mobile devices connected to the same network.


### 12. Project Status

This project is developed as an academic prototype for demonstration and
evaluation purposes. Public cloud deployment may be limited by free-tier
resource constraints.

### 13. Conclusion

The Climate Visibility Prediction System demonstrates how machine learning and
real-time weather data can be combined to support agricultural decision-making.
The project focuses on simplicity, explainability, and practical usability for farmers.

### 14. Author

Gaurav Naik

