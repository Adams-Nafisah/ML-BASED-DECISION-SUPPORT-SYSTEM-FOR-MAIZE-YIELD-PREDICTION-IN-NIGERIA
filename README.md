Maize Yield Prediction System with Explainable AI
Project Summary

This project develops an end-to-end machine learning system for predicting maize yield using environmental and soil data. The pipeline includes data analysis, feature engineering, model training, and explainability using SHAP.

Initial models showed near-perfect accuracy but were found to rely on geographic identifiers, leading to overfitting. A refined scientific model was developed using only agronomically meaningful variables, resulting in more realistic performance (R² ≈ 0.84). The final system balances predictive accuracy with interpretability and real-world applicability.

A Streamlit application is included to provide an interactive interface where users can input environmental conditions and receive yield predictions, explanations, and actionable agricultural recommendations.

project/
│

├── data/

│   └── final-data-Before FS.csv

│

├── models/

│   ├── maize_yield_ensemble.pkl

│   ├── scientific_rf.pkl

│   ├── scientific_xgb.pkl

│   ├── scientific_lgbm.pkl

│   ├── scaler.pkl

│   └── scientific_features.json
│
├── notebooks/

│   └── main_analysis.ipynb
│
├── figures/

│   ├── eda_yield_distribution.png

│   ├── eda_scatter_updated.png

│   ├── shap_scientific_summary.png

│   └── prediction_accuracy_analysis.png

├── app/
│   └── app.py
│
│
└── README.md

Setup Instructions

1. Create Environment

python -m venv venv

source venv/bin/activate   # Mac/Linux

venv\Scripts\activate      # Windows

2. Install Dependencies

pip install pandas numpy matplotlib seaborn scikit-learn xgboost lightgbm shap joblib streamlit
3. Optional (for notebook usage)

pip install jupyter

How to Run the Project
Step 1: Load Dataset

Ensure the dataset file is placed in the data/ folder:

data/final-data-Before FS.csv

Step 2: Run Notebook

Open and execute:

notebooks/01_maize_yield_modeling.ipynb
This will:

Load and clean data

Perform exploratory analysis

Engineer features

Train models

Evaluate performance

Generate visualizations

Step 3: Load Saved Models (Optional)
import joblib

model = joblib.load("models/maize_yield_ensemble.pkl")

Run Streamlit App (Recommended Interface)
streamlit run app/app.py

Reproducing Results

To reproduce results exactly:

Use the same dataset version provided

Ensure random seeds are fixed (random_state=42 used throughout)

Run cells in order from:

Data loading

Feature engineering

Train-test split

Model training

Evaluation

Key outputs that should match:

Scientific ensemble R² ≈ 0.84

MAE ≈ 0.12–0.13 range
SHAP top drivers: evaporation, temperature range, heat-water stress

Key Features Used (Scientific Model)

Average temperature

Precipitation

Soil pH

Soil texture (clay, sand, silt)

Evaporation index

Heat-water stress

Rainfall wind ratio

Moisture stress index

Model Explainability

SHAP is used to interpret both:

Global feature importance
Local (farm-level) predictions

This ensures transparency in decision-making and aligns predictions with agronomic reasoning.

Notes

Earlier high accuracy models were identified as overfitted due to leakage from geographic identifiers.

Final model prioritises generalisation and scientific validity over inflated accuracy.

All models are saved in models/ for reproducibility and deployment.
