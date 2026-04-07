# 🌽 ML-DSS for Maize Yield Prediction — Nigeria
## Complete Setup & Run Guide
**Author:** Nafisah Adams | USIU-Africa | Fall 2025

---

## 📁 Project Structure
```
maize_dss/
│
├── 01_maize_yield_modeling.ipynb   ← STEP 1: Run this first (model training)
├── app.py                          ← STEP 2: Streamlit dashboard
├── requirements.txt                ← Dependencies
├── README.md                       ← This file
│
└── models/                         ← Auto-created by notebook
    ├── stacked_ensemble.pkl
    ├── random_forest.pkl
    ├── xgboost.pkl
    ├── lightgbm.pkl
    ├── scaler.pkl
    ├── label_encoder_state.pkl
    ├── state_avg_features.csv      ← For state-only predictions
    ├── feature_cols.json
    └── model_results.csv           ← Performance metrics table
```

---

## ⚙️ Setup Instructions (VS Code)

### 1. Create virtual environment
```bash
python -m venv maize_env
# Windows:
maize_env\Scripts\activate
# Mac/Linux:
source maize_env/bin/activate
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Open in VS Code
```bash
code .
```

### 4. Set Jupyter kernel
- Open `01_maize_yield_modeling.ipynb`
- Click kernel selector (top right) → Python Environments → `maize_env`

---

## 🚀 Running the Project

### STEP 1: Train Models (Jupyter Notebook)
Open `01_maize_yield_modeling.ipynb` and run all cells:
- **Cell 1:** Imports & setup
- **Cell 2-3:** Load/generate dataset
- **Cell 4-6:** EDA & feature engineering
- **Cell 7:** Train-test split
- **Cell 8:** Train 7 models (LR, Ridge, SVR, RF, GB, XGB, LGBM)
- **Cell 9:** Train Stacked Ensemble (best model)
- **Cell 10:** Performance comparison charts
- **Cell 11:** SHAP explainability plots
- **Cell 12:** Save all models to `/models/`

> ⏱️ Expected runtime: 3–8 minutes (depending on CPU)

### STEP 2: Launch Dashboard
```bash
streamlit run app.py
```
Opens at: `http://localhost:8501`

---

## 🔧 Loading Your Own Data

In the notebook, Cell 2, replace the synthetic data with:
```python
df = pd.read_csv('your_dataset.csv')

# Required columns:
# State, District, Avg Temp (°C), Avg Humidity (%), Avg Rainfall (mm),
# Avg Wind Speed, pH, Clay (%), Sand (%), Silt (%),
# Crop Yield (MT/Ha), Hectare
```

---

## 📊 Models Compared

| Model | Type | Notes |
|-------|------|-------|
| Linear Regression | Baseline | Traditional method |
| Ridge Regression | Regularized Linear | L2 penalty |
| SVR (RBF kernel) | Kernel Method | Non-linear |
| Random Forest | Bagging Ensemble | 300 trees |
| Gradient Boosting | Boosting | Sklearn implementation |
| XGBoost | Boosting | Optimized GBM |
| LightGBM | Boosting | Fast, leaf-wise growth |
| **Stacked Ensemble** | **Stacking** | **RF+XGB+LGBM → Ridge** |

---

## 🌐 Dashboard Features

| Tab | Description |
|-----|-------------|
| 🏠 Home | Overview & system summary |
| 🔮 Yield Forecast | Full prediction + SHAP explanation |
| 🗺️ State Quick-Predict | Predict with state name only |
| 🦗 Pest & Disease Report | Submit & view outbreak reports |
| 📊 Model Performance | Compare all 8 models visually |
| 📰 Weather & News | Live agricultural news feed |
| ℹ️ About & Methods | Research methodology details |

---

## 🔬 Research Alignment

### Objectives → Implementation Mapping

| Research Objective | Implementation |
|---|---|
| 1. Analyze climate/soil influence | EDA + Correlation + Scatter plots (Cells 4-6) |
| 2. Review existing ML models | 7 baseline models trained & compared (Cell 8) |
| 3. Develop optimized ensemble | Stacked Ensemble: RF+XGB+LGBM (Cell 9) |
| 4. Compare accuracy & robustness | Performance table + visualizations (Cell 10) |
| + XAI transparency | SHAP values in notebook + dashboard (Cell 11) |
| + DSS deployment | Streamlit app with 7 tabs (app.py) |

---

## 📈 Expected Results

Based on the dataset structure, typical results:
- Linear Regression R²: ~0.75–0.85
- Random Forest R²: ~0.90–0.95
- XGBoost R²: ~0.91–0.96
- **Stacked Ensemble R²: ~0.92–0.97**

---

## 🆘 Troubleshooting

**Models not found error in Streamlit:**
→ Run the notebook completely first. Check `/models/` folder exists.

**SHAP import error:**
```bash
pip install shap --upgrade
```

**LightGBM install error on Windows:**
```bash
pip install lightgbm --install-option=--mpi
```

**Port already in use:**
```bash
streamlit run app.py --server.port 8502
```

---

*USIU-Africa | School of Science and Technology | Data Science & Analytics*
