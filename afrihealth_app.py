import joblib
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

#App Title  
st.title ('AfriHealth')
#App Subtitle
st.subheader('Hypertension Prediction App')
#App description
st.write(' Welcome to AfriHealth, your trusted companion for managing hypertension.')
st.write('Our app provides personalized insights and recommendations to help you maintain a healthy lifestyle and effectively manage your blood pressure. With AfriHealth, you can track your health data, receive tailored advice, and stay informed about your condition. ')
st.write('Take control of your health with AfriHealth today!')

#User type selection
user_type = st.selectbox('Select User Type', ['Patient/Individual', 'Healthcare Professional'])
if user_type == 'Patient/Individual':
    st.write(' As a patient or individual, you can use this app to input your health data and receive personalized insights and recommendations to help you manage your hypertension effectively.')
    st.write(' Please provide accurate information for the best results, and remember to consult with your healthcare provider for any medical concerns or conditions.')
      
else:
    st.write('As a healthcare professional, you can use this app to input your patients health data and receive insights and recommendations to assist in managing their hypertension effectively.')
    st.write('Please ensure that the information provided is accurate for the best results, and always reach out to your patients for any medical concerns or conditions.')

# Load model
model = joblib.load("hypertension_model.pkl")
# Load data
data = pd.read_csv('final_realistic_hypertension_data.csv')
X_test = data.drop(columns=['hypertension_status','systolic_bp_mmhg','diastolic_bp_mmhg'])
features = X_test.columns.tolist()
print(features)


#tells users to input their health data to predict their hypertension status
st.subheader('Input Your Health Data')
st.write(' Please enter your health data below to predict your hypertension status.  The more accurate the information you provide, the better the prediction will be. ')
st.write('Remember, this tool is for informational purposes only and should not replace professional medical advice. Always consult with a healthcare provider for any health concerns or conditions.')

# User input
age = st.number_input('age')
sex = st.selectbox('sex', ['Male', 'Female'])
sex_map = {'Female': 0, 'Male': 1}
bmi = st.number_input('bmi', help="BMI = weight (kg) ÷ height² (m²). \n Example: 70kg / (1.75 × 1.75)" )
residence = st.selectbox('residence', ['Rural','Urban'])
residence_map = {'Rural': 0, 'Urban': 1}
total_cholesterol_mg_dl = st.number_input('total_cholesterol_mg_dl')
smoking = st.selectbox('smoking', ['No', 'Yes'])
smoking_map = {'No': 0, 'Yes': 1}
diabetes = st.selectbox('diabetes', ['No', 'Yes'])
diabetes_map = {'No': 0, 'Yes': 1}
family_history_hypertension = st.selectbox('family_history_hypertension', ['No', 'Yes'])
family_history_hypertension_map = {'No': 0, 'Yes': 1}
age_group = st.selectbox('age_group', ['Young', 'Middle-aged', 'Senior'], help="Age groups are categorized as follows: Young (Below 35 years), Middle-aged (35-55 years), Senior (56 years and above).")
age_group_map = {'Young': 0, 'Middle-aged': 1, 'Senior': 2}
stress_level = st.selectbox('stress_level', ['Low', 'Medium', 'High'], help="Stress levels are categorized as follows: Low (minimal stress), Medium (occasional stress), High (frequent or chronic stress).")
stress_level_map = {'Low': 0, 'Medium': 1, 'High': 2}
income_level = st.selectbox('income_level', ['Low', 'Medium', 'High'], help="Income levels are categorized as follows: Low (limited access to healthcare or poor nutrition), Medium (Average access to healthcare and resources), High (Best access to preventive medicine and fitness resources).")
income_level_map = {'Low': 0, 'Medium': 1, 'High': 2}
education_level = st.selectbox('education_level', ['Basic', 'Secondary', 'Tertiary'])
education_level_map = {'Basic': 0, 'Secondary': 1, 'Tertiary': 2}
sleep_hours = st.number_input('sleep_hours')
alcohol_heavy = st.selectbox('alcohol_heavy', ['No', 'Yes'])
alcohol_heavy_map = {'No': 0, 'Yes': 1}
physically_active = st.selectbox('physically_active', ['No', 'Yes'])
physically_active_map = {'No': 0, 'Yes': 1}
high_salt_diet = st.selectbox('high_salt_diet', ['No', 'Yes'])
high_salt_diet_map = {'No': 0, 'Yes': 1}
diagnosed = st.selectbox('diagnosed', ['No', 'Yes'], help="Have you been previously diagnosed with hypertension by a healthcare professional?")
diagnosed_map = {'No': 0, 'Yes': 1}
on_medication = st.selectbox('on_medication', ['No', 'Yes'])
on_medication_map = {'No': 0, 'Yes': 1}
medication_adherence = st.selectbox('medication_adherence', ['Low', 'Medium', 'High'])  
medication_adherence_map = {'Low': 0, 'Medium': 1, 'High': 2}
bp_controlled = st.selectbox('bp_controlled', ['No', 'Yes'], help="Is your blood pressure controlled?")
bp_controlled_map = {'No': 0, 'Yes': 1}
stroke_history = st.selectbox('stroke_history', ['No', 'Yes'], help="Have you had a stroke before?")
stroke_history_map = {'No': 0, 'Yes': 1}
myocardial_infarction = st.selectbox('myocardial_infarction', ['No', 'Yes'], help="Have you had a myocardial infarction (heart attack) before?")
myocardial_infarction_map = {'No': 0, 'Yes': 1}
heart_failure = st.selectbox('heart_failure', ['No', 'Yes'], help="Have you been diagnosed with heart failure?")
heart_failure_map = {'No': 0, 'Yes': 1}
ldl_mg_dl = st.number_input('ldl_mg_dl', help="LDL (Low-Density Lipoprotein) cholesterol levels in mg/dL. \n Example: 100 mg/dL")
hdl_mg_dl = st.number_input('hdl_mg_dl', help="HDL (High-Density Lipoprotein) cholesterol levels in mg/dL. \n Example: 60 mg/dL")
creatine_mg_dl = st.number_input('creatine_mg_dl', help="Creatine levels in mg/dL, which can indicate kidney function. \n Example: 1.0 mg/dL")

#Create an arrayfor user input
userInput = [
    age,
    sex_map[sex],
    residence_map[residence],
    bmi,
    family_history_hypertension_map[family_history_hypertension],
    diabetes_map[diabetes],
    smoking_map[smoking],
    alcohol_heavy_map[alcohol_heavy],
    physically_active_map[physically_active],
    high_salt_diet_map[high_salt_diet],
    diagnosed_map[diagnosed],
    on_medication_map[on_medication],
    medication_adherence_map[medication_adherence],
    bp_controlled_map[bp_controlled],
    stroke_history_map[stroke_history],
    myocardial_infarction_map[myocardial_infarction],
    heart_failure_map[heart_failure],
    total_cholesterol_mg_dl,
    ldl_mg_dl,
    hdl_mg_dl,
    creatine_mg_dl,
    age_group_map[age_group],
    income_level_map[income_level],
    education_level_map[education_level],
    stress_level_map[stress_level],
    sleep_hours,
]

#Predict hypertension status
if st.button('Predict Hypertension Status'):
    prediction = model.predict([userInput])[0] # returns the first element of the array, which is the predicted class (0 or 1)
    probability = model.predict_proba([userInput])[0][1]  # Probability of the predicted class
    
    #display prediction result
    if prediction == 1:
        st.error(f'Hypertensive')
    else:
        st.success(f'Non-Hypertensive')

    #risk assessment based on probability and recommendations for patients/individuals#
    if user_type == 'Patient/Individual':
        if probability >=  0.7:
            st.error(f"High Risk of Hypertension with a probability of {probability:.2%}")

            st.subheader('Recommendation')
            st.markdown("""
            - Consult a healthcare professional immediately  
            - Monitor your blood pressure regularly  
            - Reduce salt intake  
            - Maintain a healthy lifestyle  
            """)
        elif probability >= 0.4:
            st.warning(f"Moderate Risk of Hypertension with a probability of {probability:.2%}")

            st.subheader('Recommendation')
            st.markdown("""
            - Schedule a check-up with your healthcare provider  
            - Monitor your blood pressure regularly  
            - Adopt a healthy diet and lifestyle  
            """)
        else:
            st.success(f"Low Risk of Hypertension with a probability of {probability:.2%}")

            st.subheader('Recommendation')
            st.markdown("""
            - Continue maintaining a healthy lifestyle  
            - Monitor your blood pressure regularly  
            - Schedule regular check-ups with your healthcare provider  
            """)
        
    # risk assessment based on probability and recommendations for healthcare professionals 
    if user_type == 'Healthcare Professional':
        if probability >= 0.7:
            st.error(f"High Risk of Hypertension with a probability of {probability:.2%}")

            st.subheader('Recommendation')
            st.markdown("""
            - Prioritize patient for immediate intervention  
            - Conduct further diagnostic tests  
            - Develop a comprehensive treatment plan  
            """)
        elif probability >= 0.4:
            st.warning(f"Moderate Risk of Hypertension with a probability of {probability:.2%}")

            st.subheader('Recommendation')
            st.markdown("""
            - Schedule follow-up appointments  
            - Monitor patient's blood pressure regularly  
            - Provide lifestyle modification advice  
            """)
        else:
            st.success(f"Low Risk of Hypertension with a probability of {probability:.2%}")

            st.subheader('Recommendation')
            st.markdown("""
            - Continue regular monitoring  
            - Encourage healthy lifestyle choices  
            - Schedule routine check-ups  
            """)    