import streamlit as st
import joblib
import numpy as np

scaler = joblib.load('scaler.pkl')
model = joblib.load('knn_model.pkl')

st.set_page_config(
    page_title="Customer Churn Prediction",
    page_icon=":guardsman:",
    layout="centered",
)

st.title('Customer Churn Prediction')

st.divider()

st.markdown("### Please enter the following details to predict the customer churn:")

st.divider()

age = st.number_input('👤 Age', min_value=18, max_value=100, value=18, step=1)
gender = st.radio('👫 Gender', ['Female', 'Male'])
tenure = st.number_input('📅 Tenure (Months)', min_value=0, max_value=100, value=0, step=1)
monthly_charges = st.number_input('💸 Monthly Charges', min_value=0, max_value=1000, value=50, step=1)
contract_type = st.selectbox('📃 Contract Type', ['Month-to-Month', 'One Year', 'Two Year'])
total_charges = st.number_input('💰 Total Charges', min_value=0, max_value=10000, value=200, step=1)
tech_support = st.radio('💻 Tech Support', ['Yes', 'No'])

st.divider()

predictbutton = st.button('🔮 Predict')

if predictbutton:
    if contract_type == 'Month-to-Month':
        contract_type = 0
    elif contract_type == 'One Year':
        contract_type = 1
    else:
        contract_type = 2

    tech_support = 1 if tech_support == 'Yes' else 0
    gender = 1 if gender == 'Female' else 0
    
    input_data = np.array([age, gender, tenure, monthly_charges, contract_type, total_charges, tech_support])
    
    input_data = scaler.transform([input_data])
    
    prediction = model.predict(input_data)[0]

    prediction_text = "Churn" if prediction == 1 else "Not a Churn" 
    st.markdown(f"### 📊 **Prediction Result:**")
    st.write(f"The customer is likely to be a **{prediction_text}** customer.")
    
else:
    st.write('Please click on the **Predict** button to see the result')

st.markdown("""
<style>
    .stButton > button {
        background-color: #FF7F50;
        color: white;
        font-size: 20px;
        border-radius: 10px;
        padding: 10px 20px;
    }
    .stButton > button:hover {
        background-color: #FF4500;
    }
    .stNumberInput > div > div > input {
        font-size: 18px;
        padding: 10px;
        border-radius: 5px;
    }
    .stRadio > div {
        font-size: 16px;
    }
    .stSelectbox > div {
        font-size: 16px;
    }
</style>
""", unsafe_allow_html=True)
