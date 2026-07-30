import streamlit as st
import pickle
import numpy as np

model = pickle.load(open("best_model.pkl", "rb"))

st.title("Hotel Dynamic Pricing System")

lead_time = st.slider("Lead Time", 0, 365)
guests = st.number_input("Number of Guests", 1, 5)

if st.button("Predict Price"):
    prediction = model.predict([[lead_time, guests]])
    st.success(f"Recommended Price: ${prediction[0]:.2f}")
