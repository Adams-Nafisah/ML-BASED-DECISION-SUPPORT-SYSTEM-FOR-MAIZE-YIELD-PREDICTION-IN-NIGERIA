🌽 ML-DSS for Maize Yield Prediction — Nigeria

Machine Learning–Based Decision Support System

Author: Nafisah Adams

Institution: United States International University-Africa (USIU-Africa)

Program: Data Science & Analytics

Project: Undergraduate Research Project

Semester: Spring 2026

📘 Project Overview

This project develops a Machine Learning–Based Decision Support System (ML-DSS) for predicting maize yield using environmental and soil variables.

The system applies multiple machine learning algorithms to model the relationship between climatic conditions, soil characteristics, and maize productivity. The best-performing model is deployed through an interactive Streamlit dashboard, allowing users to generate maize yield forecasts based on environmental inputs.

The project demonstrates how data science techniques can support agricultural decision-making and yield forecasting.

maize_dss/
│
├── 01_maize_yield_modeling.ipynb     
├── app.py                           
├── requirements.txt                 
├── README.md                        
│
└── models/                           
    ├── stacked_ensemble.pkl
    ├── random_forest.pkl
    ├── xgboost.pkl
    ├── scaler.pkl
    ├── label_encoder_state.pkl
    ├── feature_cols.json
    └── model_results.csv

The /models folder is automatically generated when the notebook finishes training the models.

⚙️ Setup Instructions

1️⃣ Create a Virtual Environment

python -m venv maize_env

Activate the environment:

Windows

maize_env\Scripts\activate

Mac/Linux

source maize_env/bin/activate

2️⃣ Install Project Dependencies

pip install -r requirements.txt

3️⃣ Open the Project in VS Code

code .

4️⃣ Select the Jupyter Kernel

Open:

01_maize_yield_modeling.ipynb

Then select:

Python Environment → maize_env
🚀 Running the Project
Step 1 — Train the Models

Open the notebook:

01_maize_yield_modeling.ipynb

Run all cells sequentially.

Main notebook stages:

| Stage                  | Description                            |
| ---------------------- | -------------------------------------- |
| Imports & Setup        | Load libraries and environment         |
| Dataset Loading        | Import maize dataset                   |
| Data Exploration       | Examine dataset structure              |
| Feature Engineering    | Prepare climate and soil variables     |
| Train/Test Split       | Prepare data for model training        |
| Model Training         | Train multiple ML algorithms           |
| Ensemble Model         | Train stacked ensemble model           |
| Performance Evaluation | Compare models using R² and MAE        |
| Explainability         | Generate SHAP feature importance plots |
| Model Saving           | Export trained models to `/models/`    |


Expected runtime:

3–8 minutes depending on CPU performance

Step 2 — Launch the Decision Support Dashboard

Run the Streamlit application:

streamlit run app.py

The dashboard will open in your browser at:

http://localhost:8501
📊 Machine Learning Models

The project compares several regression algorithms used in predictive modelling.

| Model                           | Type                       |
| ------------------------------- | -------------------------- |
| Linear Regression               | Baseline statistical model |
| Ridge Regression                | Regularized linear model   |
| Support Vector Regression (SVR) | Kernel-based regression    |
| Random Forest                   | Bagging ensemble model     |
| XGBoost                         | Gradient boosting model    |
| **Stacked Ensemble**            | Combined ensemble model    |


The stacked ensemble model combines multiple algorithms to improve prediction accuracy.

📈 Model Performance

Performance was evaluated using:

R² (Coefficient of Determination)
MAE (Mean Absolute Error)
The results show that ensemble models significantly outperform traditional regression models.
| Model                | R²         | MAE       |
| -------------------- | ---------- | --------- |
| Linear Regression    | -936.55    | 1.132     |
| Ridge Regression     | -1252.12   | 1.256     |
| SVR                  | 0.7500     | 0.173     |
| Random Forest        | 0.7764     | 0.148     |
| XGBoost              | 0.8409     | 0.131     |
| **Stacked Ensemble** | **0.8424** | **0.129** |


🌐 Decision Support Dashboard

The system is deployed using Streamlit, providing an interactive interface for maize yield prediction.

Dashboard Features
| Feature              | Description                                       |
| -------------------- | ------------------------------------------------- |
| Yield Prediction     | Predict maize yield based on environmental inputs |
| Model Comparison     | Visual comparison of machine learning models      |
| Feature Importance   | SHAP-based explanation of model predictions       |
| Environmental Inputs | Users enter climate and soil variables            |
| Prediction Output    | Estimated maize yield (MT/Ha)                     |


The dashboard allows users without machine learning expertise to interact with the predictive system.

📊 Dataset

The dataset used in this project was obtained from the Mendeley Data Repository.

Dataset link:

https://data.mendeley.com/datasets/dkv6b3xj99/1

The dataset contains environmental and soil variables associated with maize production, including:

Temperature

Rainfall

Wind speed

Soil composition (clay, sand, silt)

Crop yield per hectare

🔬 Research Objectives

The project addresses the following objectives:

Analyse the influence of climatic and soil variables on maize yield.

Evaluate machine learning models for crop yield prediction.

Develop an optimized ensemble model for maize yield forecasting.

Deploy a machine learning–based decision support system.

Explainable AI

To improve interpretability, the project uses SHAP (Shapley Additive Explanations).

SHAP analysis identifies which environmental variables contribute most to maize yield predictions.

This improves transparency and helps users understand how predictions are generated.

Troubleshooting

Models Not Found

Ensure the notebook has been run completely so that the /models folder is generated.

SHAP Installation Error

pip install shap --upgrade

Streamlit Port Already in Use

streamlit run app.py --server.port 8502

Technologies Used

Python

Pandas

Scikit-learn

XGBoost

SHAP

Streamlit

Jupyter Notebook


🎓 Academic Context

This project was developed as part of the Data Science & Analytics undergraduate program at USIU-Africa.

The study demonstrates how machine learning techniques can support agricultural analytics and crop yield forecasting.
