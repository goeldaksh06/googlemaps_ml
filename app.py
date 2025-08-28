import streamlit as st

st.title("🛣️ Smart Route Prediction")
st.write("Enter route details below and get predictions for travel time, fuel cost, scenic score, and safety score.")

# Input widgets with unique keys
distance = st.slider("📏 Distance (km)", 1, 100, 10, key="distance_slider")
traffic = st.selectbox("🚦 Traffic Level", ["low", "medium", "high"], key="traffic_select")
weather = st.selectbox("🌤️ Weather", ["clear", "rainy", "foggy"], key="weather_select")
time_of_day = st.selectbox("🕒 Time of Day", ["morning", "afternoon", "evening", "night"], key="time_select")
road_type = st.selectbox("🛣️ Road Type", ["city", "highway", "rural"], key="road_select")

# Dummy predictions (replace with your ML model)
predicted_travel_time = distance * 1.5  # Example calculation
predicted_fuel_cost = distance * 0.39
predicted_scenic_score = 0.55
predicted_safety_score = 0.40

# Display predicted metrics
st.subheader("📊 Predicted Route Metrics")
st.metric("⏱️ Travel Time (min)", f"{predicted_travel_time:.2f}")
st.metric("⛽ Fuel Cost", f"{predicted_fuel_cost:.2f}")
st.metric("🌄 Scenic Score", f"{predicted_scenic_score:.2f}")
st.metric("🛡️ Safety Score", f"{predicted_safety_score:.2f}")

# Optional: Visualize metrics
import matplotlib.pyplot as plt

metrics = {
    "Travel Time": predicted_travel_time,
    "Fuel Cost": predicted_fuel_cost,
    "Scenic Score": predicted_scenic_score,
    "Safety Score": predicted_safety_score
}

fig, ax = plt.subplots()
ax.bar(metrics.keys(), metrics.values(), color=['skyblue','orange','green','red'])
ax.set_ylim(0, max(metrics.values())*1.2)
st.pyplot(fig)
