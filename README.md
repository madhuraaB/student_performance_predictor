# 🎓 Student Performance Predictor

### Live Demo

https://studentperformancepredictor-dlwto5sjqs6lkwwqx5de79.streamlit.app/

---

## Overview

This project is a Machine Learning-based web application that predicts a student's exam performance based on academic, behavioral, and environmental factors.

The system analyzes important student-related attributes such as:

* Hours Studied
* Attendance
* Previous Scores
* Tutoring Sessions
* Sleep Hours
* Motivation Level
* Access to Resources
* Parental Involvement

and predicts the student's expected exam score and performance level.

---

## Features

* Data preprocessing and cleaning
* Feature engineering
* Machine Learning model training
* Model comparison and evaluation
* Student performance prediction
* Interactive Streamlit web application
* Real-time performance prediction

---

## Technologies Used

* Python
* Pandas
* NumPy
* Scikit-Learn
* XGBoost
* Matplotlib
* Streamlit
* Pickle

---

## Machine Learning Models Used

* Linear Regression
* Random Forest Regressor
* XGBoost Regressor

---

## Dataset

Student Performance Dataset
Link:https://www.kaggle.com/datasets/ayeshaseherr/student-performance

### Features

* Hours_Studied
* Attendance
* Previous_Scores
* Tutoring_Sessions
* Sleep_Hours
* Access_to_Resources
* Motivation_Level
* Teacher_Quality
* Parental_Involvement
* Family_Income
* Internet_Access
* Peer_Influence
* Physical_Activity
* Distance_from_Home
* Parental_Education_Level

### Target Variable

Exam_Score

---

## Data Cleaning

The dataset was cleaned by:

* Handling missing values
* Removing duplicate records
* Removing contradictory records
* Reducing label noise
* Removing unrealistic score combinations

---

## Feature Engineering

Additional features were created to improve model performance:

* Study_Efficiency
* Academic_Consistency
* Study_Commitment

---

## Model Performance

| Model             | R² Score |
| ----------------- | -------- |
| Linear Regression | 0.71     |
| Random Forest     | 0.62     |
| XGBoost           | 0.67     |

### Selected Model

Linear Regression was selected for deployment because it produced the most stable and interpretable predictions.

---

## Application Inputs

The user provides:

* Hours Studied
* Attendance
* Previous Scores
* Tutoring Sessions
* Sleep Hours
* Access to Resources
* Motivation Level
* Parental Involvement

The application automatically generates additional features and predicts student performance.

---
## Project Structure

```text
student_performance_predictor/
│
├── app.py
├── model.pkl
├── columns.pkl
├── requirements.txt
├── README.md
│
├── dataset/
│   ├── dataset.csv
│   └── cleaned_dataset.csv
│
├── notebooks/
│   ├── data_cleaning.ipynb
│   └── model_training.ipynb
    └── eda_visulaization.ipynb

│
└── Screenshots/
```

---

## Installation

### Clone Repository

```bash
git clone https://github.com/madhuraaB/student_performance_predictor.git
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Streamlit App

```bash
streamlit run app.py
```

---

## Future Improvements

* Improve dataset quality
* Hyperparameter tuning
* Explainable AI visualizations
* Enhanced UI/UX
* Additional student-related features

---

## Conclusion

This project demonstrates the application of Machine Learning techniques for predicting student academic performance and provides an interactive platform for analyzing factors that influence exam outcomes.

---

## Author

**Madhura Bhuvad**

