
An AI-powered Predictive Maintenance System that predicts industrial machine failure using Machine Learning and real-time sensor data.

The system analyzes machine operating conditions and predicts whether the machine is healthy or has a possible failure risk. It helps industries perform preventive maintenance before unexpected breakdowns occur.

---

## Dashboard Preview

![Dashboard](screenshots/dashboard.png)

---

# Project Overview

Industrial machines continuously generate sensor information such as temperature, speed, torque, and tool usage.

Unexpected machine failure can lead to:

- Production downtime
- Increased maintenance cost
- Reduced efficiency

This project applies Machine Learning techniques to predict machine failure conditions and provides maintenance recommendations through a web-based monitoring dashboard.

---

# Features

- Real-time machine failure prediction
- Industrial sensor monitoring dashboard
- Failure probability calculation
- AI-based maintenance recommendation
- Interactive slider control
- Manual sensor value input
- Light and Dark theme support
- Machine status monitoring
- FastAPI backend integration

---

# Dataset

Dataset:

AI4I 2020 Predictive Maintenance Dataset


Dataset Size:

```
Total Records : 10000

Normal Machine Records : 9661

Failure Records : 339
```

---

# Input Features

The machine learning model uses:

| Feature | Description |
|-|-|
| Air Temperature | Machine surrounding temperature |
| Process Temperature | Operating temperature |
| Rotational Speed | Machine RPM |
| Torque | Machine load |
| Tool Wear | Tool usage duration |

---

# Machine Learning Workflow


```
Dataset

   ↓

Data Cleaning

   ↓

Exploratory Data Analysis

   ↓

Feature Selection

   ↓

Train Test Split

   ↓

Model Training

   ↓

Model Comparison

   ↓

Best Model Selection

   ↓

Model Deployment

   ↓

FastAPI + React Integration
```

---

# Data Preprocessing

Performed preprocessing steps:

- Removed unnecessary columns
- Checked missing values
- Selected important sensor features
- Feature scaling using StandardScaler
- Stratified train-test splitting

---

# Class Imbalance Handling

The dataset contains imbalance:

```
Healthy Machines : 9661

Failure Machines : 339
```

Accuracy alone is not enough for this problem.

Methods analyzed:

- SMOTE Oversampling
- Class Weight Balancing
- Stratified Splitting


Final approach:

```
RandomForestClassifier(
class_weight="balanced"
)
```

Reason:

Class weight balancing improved failure detection without creating artificial synthetic failure records.

---

# Machine Learning Models Compared


| Algorithm | Accuracy |
|-|-|
| Random Forest | 98.5% |
| XGBoost | 98.4% |
| Decision Tree | 97.8% |
| SVM | 97.2% |
| Logistic Regression | 96.85% |


---

# Final Selected Model

## Random Forest Classifier

Random Forest was selected because it achieved:

- High accuracy
- Better failure identification
- Good precision and recall balance
- Stable performance on sensor data
- Lower false predictions

---

# Model Performance Evaluation


Evaluation metrics used:

- Accuracy
- Precision
- Recall
- F1 Score
- Confusion Matrix


---

# Random Forest Classification Report


| Class | Precision | Recall | F1 Score | Support |
|-|-|-|-|-|
| Healthy Machine (0) | 0.99 | 1.00 | 0.99 | 1932 |
| Failure Machine (1) | 0.87 | 0.60 | 0.71 | 68 |


---

# Overall Performance


| Metric | Score |
|-|-|
| Accuracy | 98% |
| Macro Precision | 0.93 |
| Macro Recall | 0.80 |
| Macro F1 Score | 0.85 |
| Weighted Precision | 0.98 |
| Weighted Recall | 0.98 |
| Weighted F1 Score | 0.98 |

---

# Confusion Matrix


```
                Predicted

             Healthy   Failure


Actual Healthy

              1926        6


Actual Failure

                27       41

```


Explanation:

- Correct Healthy Predictions : 1926
- Correct Failure Predictions : 41
- False Failure Alerts : 6
- Missed Failure Cases : 27


---

# System Architecture


```
React Dashboard

        |
        |
        ↓

FastAPI Backend

        |
        |
        ↓

Machine Learning Model

        |
        |
        ↓

Prediction Result

        |
        |
        ↓

Maintenance Recommendation
```

---

# Backend API


Backend Framework:

FastAPI


## Machine Data API


```
GET /machine
```


Returns:

- Machine ID
- Temperature
- RPM
- Torque
- Tool Wear


---


## Prediction API


```
POST /predict
```


Returns:


```
{
Prediction Status,

Failure Probability,

Maintenance Recommendation
}
```


---

# Frontend Dashboard


Developed using:

- React
- TypeScript
- Axios
- CSS


Dashboard includes:

- Sensor input panel
- Prediction result card
- Machine status table
- Theme switching
- Real-time API communication


---

# Technology Stack


## Machine Learning

- Python
- Pandas
- NumPy
- Scikit-Learn
- XGBoost
- Matplotlib
- Seaborn
- Joblib


## Backend

- FastAPI
- Uvicorn
- Pydantic


## Frontend

- React
- TypeScript
- Axios
- CSS


---

# Project Structure


```
AI-Predictive-Maintenance

│
├── backend
│
│   ├── main.py
│   ├── model.pkl
│   ├── scaler.pkl
│   └── requirements.txt
│
│
├── frontend
│
│   └── src
│
│       ├── App.tsx
│       └── App.css
│
│
├── ml
│
│   ├── dataset
│   └── model_training.ipynb
│
│
├── screenshots
│
│   └── dashboard.png
│
└── README.md

```


---

# How To Run


## Backend


Move to backend folder:


```bash
cd backend
```


Install dependencies:


```bash
pip install -r requirements.txt
```


Run server:


```bash
python -m uvicorn main:app --reload
```


Server:

```
http://127.0.0.1:8000
```


---

## Frontend


Move to frontend:


```bash
cd frontend
```


Install packages:


```bash
npm install
```


Start React:


```bash
npm run dev
```


Application:

```
http://localhost:5173
```


---

# Sample Prediction Output


```
Machine Status:

Healthy Machine


Failure Probability:

4.62%


Recommendation:

Machine condition is normal.
Continue monitoring.

```


---

# Future Improvements


- IoT sensor integration
- Real-time industrial data streaming
- Cloud deployment
- Alert notification system
- Deep learning based prediction


---

# Conclusion


The AI Predictive Maintenance System successfully predicts machine failure risks using industrial sensor data.

The integration of Machine Learning, FastAPI, and React provides a complete end-to-end intelligent monitoring solution for preventive maintenance.

---
