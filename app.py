import streamlit as st
import pandas as pd
import joblib

# Load the trained pipeline
pipeline = joblib.load("route_model.pkl")

st.title("🚗 Smart Route Predictor")
st.write("Enter your route details to get predictions for travel time, fuel cost, scenic score, and safety score.")

# User Inputs
distance = st.number_input("Distance (km)", min_value=1, max_value=500, value=50)
traffic = st.selectbox("Traffic Level", ["low", "medium", "high"])
weather = st.selectbox("Weather", ["clear", "rainy", "foggy"])
time_of_day = st.selectbox("Time of Day", ["morning", "afternoon", "evening", "night"])
road_type = st.selectbox("Road Type", ["highway", "city", "rural"])

# Make DataFrame
user_input = pd.DataFrame(
    [[distance, traffic, weather, time_of_day, road_type]],
    columns=["distance_km", "traffic_level", "weather", "time_of_day", "road_type"]
)

# Predict button
if st.button("Predict Route Metrics"):
    prediction = pipeline.predict(user_input)[0]
    st.subheader("📊 Predicted Route Metrics")
    st.write(f"⏱️ Travel Time (min): **{prediction[0]:.2f}**")
    st.write(f"⛽ Fuel Cost: **{prediction[1]:.2f}**")
    st.write(f"🌄 Scenic Score: **{prediction[2]:.2f}**")
    st.write(f"🛡️ Safety Score: **{prediction[3]:.2f}**")
