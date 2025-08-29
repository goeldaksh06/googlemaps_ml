import streamlit as st
import joblib
import pandas as pd


# ✅ Add all the sklearn components you used in training
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
# (add others if you used them)

# Now load your model
pipeline = joblib.load("route_model.pkl")


# Load trained model pipeline
pipeline = joblib.load("route_model.pkl")

st.set_page_config(page_title="Route Predictor", page_icon="🛣️", layout="centered")

st.title("🛣️ Smart Route Prediction")
st.write("Enter route details below and get predictions for travel time, fuel cost, scenic score, and safety score.")

# --- User Inputs ---
distance = st.slider("📏 Distance (km)", 1, 100, 10)

traffic = st.selectbox("🚦 Traffic Level", ["low", "medium", "high"])
weather = st.selectbox("🌤️ Weather", ["clear", "rainy", "foggy"])
time_of_day = st.selectbox("🕒 Time of Day", ["morning", "afternoon", "evening", "night"])
road_type = st.selectbox("🛣️ Road Type", ["highway", "city", "rural"])

# Create dataframe for model
user_input = pd.DataFrame({
    "distance_km": [distance],
    "traffic_level": [traffic],
    "weather": [weather],
    "time_of_day": [time_of_day],
    "road_type": [road_type],
})

# --- Prediction ---
if st.button("🔮 Predict"):
    prediction = pipeline.predict(user_input)

    # Show metrics in dashboard style
    st.subheader("📊 Predicted Route Metrics")
    col1, col2 = st.columns(2)
    col1.metric("⏱️ Travel Time (min)", f"{prediction[0][0]:.2f}")
    col2.metric("⛽ Fuel Cost", f"{prediction[0][1]:.2f}")

    col3, col4 = st.columns(2)
    col3.metric("🌄 Scenic Score", f"{prediction[0][2]:.2f}")
    col4.metric("🛡️ Safety Score", f"{prediction[0][3]:.2f}")

    # Bar chart visualization
    results_df = pd.DataFrame({
        "Metric": ["Travel Time (min)", "Fuel Cost", "Scenic Score", "Safety Score"],
        "Value": prediction[0]
    })
    st.bar_chart(results_df.set_index("Metric"))

import streamlit as st
import pandas as pd
import joblib

# Load trained model pipeline
pipeline = joblib.load("route_model.pkl")

st.set_page_config(page_title="Route Predictor", page_icon="🛣️", layout="centered")

st.title("🛣️ Smart Route Prediction")
st.write("Enter route details below and get predictions for travel time, fuel cost, scenic score, and safety score.")

# --- User Inputs ---
distance = st.slider("📏 Distance (km)", 1, 100, 10)

traffic = st.selectbox("🚦 Traffic Level", ["low", "medium", "high"])
weather = st.selectbox("🌤️ Weather", ["clear", "rainy", "foggy"])
time_of_day = st.selectbox("🕒 Time of Day", ["morning", "afternoon", "evening", "night"])
road_type = st.selectbox("🛣️ Road Type", ["highway", "city", "rural"])

# Create dataframe for model
user_input = pd.DataFrame({
    "distance_km": [distance],
    "traffic_level": [traffic],
    "weather": [weather],
    "time_of_day": [time_of_day],
    "road_type": [road_type],
})

# --- Prediction ---
if st.button("🔮 Predict"):
    prediction = pipeline.predict(user_input)

    # Show metrics in dashboard style
    st.subheader("📊 Predicted Route Metrics")
    col1, col2 = st.columns(2)
    col1.metric("⏱️ Travel Time (min)", f"{prediction[0][0]:.2f}")
    col2.metric("⛽ Fuel Cost", f"{prediction[0][1]:.2f}")

    col3, col4 = st.columns(2)
    col3.metric("🌄 Scenic Score", f"{prediction[0][2]:.2f}")
    col4.metric("🛡️ Safety Score", f"{prediction[0][3]:.2f}")

    # Bar chart visualization
    results_df = pd.DataFrame({
        "Metric": ["Travel Time (min)", "Fuel Cost", "Scenic Score", "Safety Score"],
        "Value": prediction[0]
    })
    st.bar_chart(results_df.set_index("Metric"))

