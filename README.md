# 🌱 AI-Based Air Quality Prediction System

---

## 📘 Project Overview

The **AI-Based Air Quality Prediction System** is a sustainability-driven machine learning project that predicts the **Air Quality Index (AQI)** of major Indian cities using environmental and pollutant data.

This initiative aims to raise awareness about air pollution and provide actionable insights to support cleaner, healthier cities using **AI for Green Skills**.

---

## 🎯 Problem Statement

Air pollution has become a critical challenge in metropolitan and industrial regions.  
This project focuses on:

- Predicting AQI using pollutant concentration levels.
- Understanding the key factors affecting air quality.
- Contributing toward sustainable environmental monitoring solutions.

---

## 🧠 Project Objectives

- Analyze and preprocess large-scale air quality datasets.
- Train and evaluate machine learning models for AQI prediction.
- Visualize trends and provide interpretable results for better decision-making.
- Develop a simple web-based interface for user interaction (Week 4 goal).

---

## 🗓️ Timeline

| **Week**   | **Agenda**                              | **Deliverables**                                                                                                            |
| ---------- | --------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- |
| **Week 1** | Problem Statement & Dataset Exploration | Defined project, selected dataset (`city_day.csv`), analyzed missing values, duplicates, data info, and summary statistics. |
| **Week 2** | Data Preprocessing & Model Training     | Clean data, feature selection, model training using ML algorithms.                                                          |
| **Week 3** | Model Evaluation & Optimization         | Evaluate model performance, tune hyperparameters, visualize results.                                                        |
| **Week 4** | UI Development & Final Submission       | Build Streamlit dashboard / presentation & submit final model.                                                              |

---

## 🧾 Dataset Information

**Source:** [Kaggle – Air Quality Data in India (2015–2020)](https://www.kaggle.com/datasets/rohanrao/air-quality-data-in-india)  
**Files Used:**

- `city_day.csv` – Daily air quality data for each Indian city.
- `city_hour.csv` – Hourly data (optional for visualization).

**Key Features:**

- Pollutants: `PM2.5`, `PM10`, `NO`, `NO2`, `NH3`, `CO`, `SO2`, `O3`, etc.
- Meteorological data: `Temperature`, `WindSpeed`, `Humidity`.
- Target variable: `AQI`, `AQI_Bucket`.

---

## 📊 Week 1 Results

### ✅ Exploratory Data Analysis

- Imported and viewed dataset using `pandas`.
- Checked for missing values, duplicates, and data types.
- Observed pollutant distribution and AQI trends.
- Exported a smaller version `city_day_sample.csv` for GitHub upload.

### 📈 Example Outputs

| Step           | Method                  | Result                          |
| -------------- | ----------------------- | ------------------------------- |
| Data Preview   | `df.head()`             | Shows first 5 records           |
| Info Summary   | `df.info()`             | Confirms 29 columns             |
| Missing Values | `df.isnull().sum()`     | Some missing pollutant readings |
| Duplicates     | `df.duplicated().sum()` | Few duplicates found            |

---

## ⚙️ Week 2 – Data Preprocessing & Model Training

### 🧹 Data Preprocessing Steps

- Dropped irrelevant columns: `City`, `Date`, and `AQI_Bucket`
- Replaced missing values using **median imputation** (robust against outliers)
- Separated **features (X)** and **target (y = AQI)**
- Scaled numerical features using **StandardScaler**
- Split data into **training (80%)** and **testing (20%)** sets

### 🧠 Model Training

Trained two regression models:

1. **Linear Regression** – baseline model
2. **Random Forest Regressor** – ensemble model for non-linear relationships

### 📈 Model Evaluation Results

| Model                       | MAE ↓     | MSE ↓       | R² ↑     |
| --------------------------- | --------- | ----------- | -------- |
| Linear Regression           | 29.91     | 2965.68     | 0.81     |
| **Random Forest Regressor** | **19.96** | **1842.74** | **0.88** |

✅ **Best Model:** Random Forest Regressor  
💾 **Saved as:** `air_quality_model.pkl`

---

### 🧾 Interpretation

- Random Forest performed significantly better due to its ability to model non-linear patterns.
- The model achieved **R² = 0.88**, indicating strong predictive accuracy.
- AQI predictions are now ready for further tuning and visualization in **Week 3**.

---

## ⚙️ Tech Stack

- **Python 3.x**
- **Pandas, NumPy, Matplotlib, Seaborn, Scikit-Learn**
- **Jupyter Notebook / Google Colab**
- **Streamlit**

---

## 🚀 How to Run

1. Clone this repository
   ```bash
   git clone https://github.com/Astlejoe789/AI-Based-Air-Quality-Prediction-System.git
   cd AI-Based-Air-Quality-Prediction-System
   ```

---

## 📚 Future Enhancements

Integrate real-time AQI data via APIs

Deploy web dashboard using Streamlit

Add city-wise pollution heatmaps and prediction insights

---

🏁 Acknowledgment

This project is part of the Shell–Edunet Skills4Future Internship under AICTE.
Grateful to mentors and Edunet Foundation for guidance in applying AI for sustainability.

---

👤 Author

ASTLE JOE A S

B.Tech. Artificial Intelligence and Machine Learning (AIML)

GitHub Profile
**ASTLE JOE A S**  
[Visit My GitHub →](https://github.com/Astlejoe789)
