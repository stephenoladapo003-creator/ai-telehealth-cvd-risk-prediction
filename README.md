# AI-Powered Telehealth System for Hypertension and Cardiovascular Disease Risk Screening

## Live Demo
[Click Here to Access the Hypertension Risk Predictor](https://ai-telehealth-cvd-risk-prediction-haccwzsqr5nfs4shytjceh.streamlit.app/)

---

## Project Description
This project is an AI-powered telehealth system designed to predict hypertension risk in individuals across Africa. Using machine learning classification models the system analyzes individual patient data including clinical, lifestyle and socioeconomic features to classify risk — enabling early detection before serious complications occur.

The application is named AfriHealth and serves two user types:
- Patient/Individual — for personal risk assessment from home
- Healthcare Professional — for clinical screening and patient prioritization

---

## Problem Statement
Hypertension and cardiovascular disease are among the leading causes of death across Africa yet most cases go undetected until a stroke or heart attack has already occurred. Key barriers include:

- Late diagnosis
- Poor routine screening
- High stroke rates
- Shortage of healthcare workers
- Poor data systems and low insurance penetration

This project addresses these challenges by providing an accessible AI-powered risk screening solution that requires no laboratory equipment.

---

## Aim
To develop a machine learning model that predicts hypertension risk in individuals using clinical, lifestyle and socioeconomic inputs, supporting early detection and improving healthcare accessibility in Africa.

---

## Objectives
1. Investigate the prevalence and diagnostic challenges of hypertension and cardiovascular disease across African healthcare settings
2. Collect and preprocess a relevant dataset with clinical, lifestyle and socioeconomic features suitable for machine learning classification
3. Develop and train Logistic Regression and Random Forest models for hypertension risk prediction
4. Evaluate and compare model performance using Accuracy, Precision, Recall and F1 Score
5. Deploy the best performing model as an accessible web application for individuals and healthcare professionals

---

## Dataset
- Source: Synthesized and engineered version of a Hypertension Risk dataset originally sourced from health records and enhanced with lifestyle and socioeconomic features
- Size: 2,000 rows and 13 columns after feature engineering
- Type: Cleaned and engineered patient data with zero null values
- Target Column: Hypertension status — Hypertensive or Non-Hypertensive

---

## Features Used

**Personal and Demographic Features:**
- Age
- Sex
- Age Group — Junior, Adult, Senior

**Health and Lifestyle Features:**
- BMI
- Smoking Status
- Sleep Hours
- Alcohol Heavy
- Physically Active
- High Salt Diet

**Medical History Features:**
- Stroke History
- Myocardial Infarction
- Heart Failure
- Family History of Hypertension

**Laboratory Measurements:**
- Total Cholesterol mg/dL
- LDL mg/dL
- HDL mg/dL
- Creatine mg/dL

**Socioeconomic and Psychosocial Features:**
- Residence — Urban or Rural
- Income Level — Low, Medium, High
- Education Level
- Stress Level — Low, Medium, High

---

## Data Cleaning and Preprocessing
- Missing Values: Handled via mean and mode imputation — final dataset has zero null values
- Duplicates: Removed all redundant patient entries
- Label Encoding: Applied to categorical columns — Sex, Residence Type and other binary columns encoded as 0 or 1
- Feature Engineering: Created age_group, stress_level, income_level and sleep_hours using numpy based on medical probability correlations to transition the project from a clinical tool to a lifestyle risk predictor

---

## Models Used
- Logistic Regression — Baseline model for comparison. Simple, fast and interpretable
- Random Forest Classifier — Final and best performing model. Handles complex non-linear relationships between lifestyle features and hypertension risk

---

## Model Results

| Model | Accuracy | Precision | Recall | F1 Score |
|---|---|---|---|---|
| Logistic Regression | 82.45% | 0.81 | 0.79 | 0.80 |
| Random Forest | 90.15% | 0.89 | 0.91 | 0.90 |

**Best Model:** Random Forest Classifier

**Why Random Forest performed better:**
Random Forest captured complex non-linear relationships between lifestyle factors like stress, BMI and sleep hours that Logistic Regression could not handle effectively.

**Hyperparameter Tuning:**
- n_estimators = 100
- random_state = 42
- Applied to ensure model stability and prevent overfitting

**Saved Model:** best_hypertension_model_RandomForest.pkl

---

## Overfitting Prevention
Three techniques were applied to ensure model reliability despite the small dataset size:

1. Cross Validation — Data was split multiple times to confirm consistent performance across different data chunks
2. Random Forest Regularization — Tree depth was limited to prevent the model from memorizing individual rows
3. Stratified Splitting — Equal representation of hypertensive and non-hypertensive patients maintained in both training and testing sets to prevent class imbalance bias

---

## Deployment
- Platform: Streamlit Community Cloud
- Application Name: AfriHealth
- Live Link: https://ai-telehealth-cvd-risk-prediction-haccwzsqr5nfs4shytjceh.streamlit.app/

**User Types:**
- Patient/Individual — personal risk assessment from home
- Healthcare Professional — clinical screening and patient prioritization

**App Output:**
- Hypertension Status — Hypertensive or Non-Hypertensive
- Probability Score — Model confidence percentage
- Recommendation — Personalized health advice based on risk level

---

## AI Ethics
The sex and residence type columns were specifically examined to ensure the model does not unfairly flag one demographic group over another. Fairness and ethical AI practice were considered throughout the model development process.

---

## Challenges Faced
- Data Leakage: Systolic blood pressure was initially included causing 100% accuracy. This column was dropped to ensure realistic and honest predictions
- Synthetic Feature Generation: Stress level, income level and sleep hours were engineered using numpy based on medical probability correlations — acknowledged as a limitation
- Class Imbalance: Addressed using stratified splitting to ensure equal class representation
- Version Control: Managing merge conflicts during simultaneous UI development
- Internet Connectivity: DNS issues encountered when pushing to GitHub

---

## Limitations
- Dataset size is limited to 2,000 samples — more diverse clinical data would improve accuracy
- Some features like stress level rely on user reported data which can be subjective
- Engineered lifestyle features were synthetically generated — real world data collection would improve model reliability
- Model predictions should be used as a screening tool only and not as a replacement for professional medical diagnosis

---

## Future Work
- Integrate real time IoT data from devices like ESP32 for live health monitoring
- Expand model to predict other cardiovascular risks beyond hypertension
- Deploy on a cloud platform such as AWS or Heroku for global accessibility
- Source larger and more diverse Africa specific datasets
- Collect real world lifestyle and socioeconomic data to replace synthetically generated features

---

## How to Run Locally

1. Clone the repository
git clone https://github.com/stephenoladapo003/ai-telehealth-cvd-risk-prediction

2. Install required libraries
pip install -r requirements.txt

3. Run the app
streamlit run app.py

---

## Team
Team AfriHealth— TechCrush AI/ML Capstone Project 2026

| Name | Role |
|---|---|
| Oladapo Stephen | Project Lead |
| Lola Owolabi | Model Engineering and Documentation |
| Adediran Adedoyin Rahman | Dataset Cleaning |
| Olagunju Amina Busayo | Streamlit Deployment |
| Temitayo Dada | Streamlit Development |
| Omojola Boluwatife Charles | Data Preprocessing |
| Adekunrun Janet | Model Engineering |
| Atinuke Mubarak Eniola | ML and Pipeline Engineering |
| Oluwadare Elizabeth Aderike | Dataset Cleaning |
| Mbonu Hilda Omon | ML and Pipeline Engineering |
| Opemipo Awolana | Streamlit Development |
| Blessing Effiong Abatai | ML and Pipeline Engineering |
| Sodiq Abdulazeez | ML and Pipeline Engineering |

---

## Acknowledgements
- TechCrush for facilitating this AI/ML program
- Our tutors and mentors for their guidance throughout this journey
- All team members for their dedication and hard work in bringing this project to life
