import streamlit as st
import pickle
import numpy as np

# Load model
model = pickle.load(open('model.pkl', 'rb'))

st.title("Telecom Churn Prediction")

account_length = st.number_input("Account Length")
total_day_minutes = st.number_input("Total Day Minutes")
customer_service_calls = st.number_input("Customer Service Calls")

if st.button("Predict"):

    data = np.array([[account_length,
                      total_day_minutes,
                      customer_service_calls]])

    prediction = model.predict(data)

    if prediction[0] == 1:
        st.error("Customer Will Churn")
    else:
        st.success("Customer Will Stay")
