# 🏭 FactoryIQ: ML-Driven Supplier Defect Impact Predictor

This project leverages machine learning to analyze and predict the impact of supplier-induced defects on manufacturing performance. By identifying defect patterns early, businesses can make data-driven decisions to improve quality control and supply chain resilience.

---

## 🌐 Live Demo

👉 **Try the interactive app here**: [FactoryIQ ML App – Streamlit](https://factoryiq-mldrivensupplierdefectimpactpredictor.streamlit.app/)  

---

## 📌 Problem Statement

### Business Context:
A manufacturing firm receives components from multiple suppliers. Some components frequently cause defects, leading to delays, increased costs, and customer dissatisfaction.

### Objective:
Build a machine learning system that predicts whether a supplier-related defect will result in a high-impact issue, supporting proactive supplier selection and quality assurance.

---

## 📊 Dataset Description

| Feature Name           | Description                                      |
|------------------------|--------------------------------------------------|
| `defect_name`          | Type of defect observed                          |
| `supplier_name`        | Name of the supplier involved                    |
| `frequency`            | Frequency of defect occurrence                   |
| `criticality`          | Severity/impact level of the defect              |
| `avg_delay_days`       | Average delay caused by the defect (in days)     |
| `inspection_pass_rate` | Historical inspection pass rate for the supplier |
| `cost_impact`          | Estimated cost impact of the defect              |
| `impact_label`         | Target variable: High (1) or Low (0) impact      |

---

## 🔍 Workflow

1. 📂 Data Preprocessing
   - Handle missing values
   - Encode categorical variables
   - Feature engineering

2. 📈 Exploratory Data Analysis
   - Defect distribution by supplier
   - Criticality and cost correlation
   - Delay heatmaps

3. 🤖 Model Training
   - Models used: Decision Tree, Random Forest, AdaBoost, Gradient Boosting, XGBoost
   - Evaluation on MAE, RMSE, R²

4. 🎯 Hyperparameter Tuning
   - XGBoost optimized with **Optuna**


---

## ⚙️ Model Performance Comparison

| Model                   | Train MAE | Test MAE | Train RMSE | Test RMSE | Train R² | Test R² |
|------------------------|-----------|----------|------------|-----------|----------|---------|
| **Decision Tree**       | 11.08     | 235.85   | 107.12     | 677.35    | 1.00     | 0.82    |
| **Random Forest**       | 78.46     | 207.96   | 204.26     | 524.83    | 0.98     | 0.89    |
| **AdaBoost**            | 315.92    | 327.34   | 505.32     | 525.90    | 0.90     | 0.89    |
| **Gradient Boosting**   | 170.00    | 190.32   | 434.29     | 487.61    | 0.92     | 0.91    |
| **XGBoost (Default)**   | 132.39    | 230.30   | 308.68     | 530.08    | 0.96     | 0.89    |

---

✅ **Tuned XGBoost** gave the best results with **Test R² of 0.907**, showing strong predictive performance with minimal overfitting.

---

