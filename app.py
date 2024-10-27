import streamlit as st
import numpy as np

# Title and Description
st.title("Glucose Level Assessment and HbA1c Estimation")
st.write("""
This app helps you assess your glucose levels, provides health advice, and estimates your HbA1c based on input values.
""")

# Input fields
st.header("Enter Your Glucose Data")
fasting_glucose = st.number_input("Fasting Glucose Level (mg/dL)", min_value=0)
postprandial_glucose = st.number_input("Postprandial Glucose Level (mg/dL)", min_value=0)
random_glucose = st.number_input("Random Glucose Level (mg/dL)", min_value=0)

# Calculate estimated HbA1c
def calculate_hba1c(avg_glucose):
    return (avg_glucose + 46.7) / 28.7

# Health advice based on glucose levels
def health_advice(fasting, postprandial, random):
    advice = ""
    if fasting < 70:
        advice += "Low fasting glucose detected; consult your healthcare provider.\n"
    elif fasting > 130:
        advice += "High fasting glucose detected; monitor and manage dietary intake.\n"
    else:
        advice += "Fasting glucose is within a healthy range.\n"
    
    if postprandial > 180:
        advice += "High postprandial glucose detected; consider lowering sugar and carb intake.\n"
    elif postprandial < 70:
        advice += "Low postprandial glucose; consult your healthcare provider.\n"
    else:
        advice += "Postprandial glucose is within a healthy range.\n"

    if random > 200:
        advice += "High random glucose detected; monitor your glucose levels regularly.\n"
    elif random < 70:
        advice += "Low random glucose; consider discussing with your doctor.\n"
    else:
        advice += "Random glucose is within a healthy range.\n"
    
    return advice

# Button to calculate results
if st.button("Assess & Estimate HbA1c"):
    # Average glucose for HbA1c estimation
    avg_glucose = np.mean([fasting_glucose, postprandial_glucose, random_glucose])
    estimated_hba1c = calculate_hba1c(avg_glucose)
    advice = health_advice(fasting_glucose, postprandial_glucose, random_glucose)

    st.subheader("Results")
    st.write(f"**Estimated HbA1c:** {estimated_hba1c:.2f}%")
    st.write("**Health Advice:**")
    st.write(advice)
