
import pandas as pd
import joblib

# Load pipeline (preprocessing + model together)
pipeline = joblib.load("route_model.pkl")

# Take user input
distance_km = float(input("Enter distance in km: "))

traffic_level = input("Enter traffic level (low/medium/high): ").strip().lower()
weather = input("Enter weather (clear/rainy/foggy): ").strip().lower()
time_of_day = input("Enter time of day (morning/afternoon/evening/night): ").strip().lower()
road_type = input("Enter road type (highway/city/rural): ").strip().lower()

# Put inputs into DataFrame
user_input = pd.DataFrame([{
    "distance_km": distance_km,
    "traffic_level": traffic_level,
    "weather": weather,
    "time_of_day": time_of_day,
    "road_type": road_type
}])

# Predict
prediction = pipeline.predict(user_input)[0]

print("\nPredicted Route Metrics:")
print(f"Travel Time (min): {prediction[0]:.2f}")
print(f"Fuel Cost: {prediction[1]:.2f}")
print(f"Scenic Score: {prediction[2]:.2f}")
print(f"Safety Score: {prediction[3]:.2f}")

import pandas as pd
import joblib

# Load pipeline (preprocessing + model together)
pipeline = joblib.load("route_model.pkl")

# Take user input
distance_km = float(input("Enter distance in km: "))

traffic_level = input("Enter traffic level (low/medium/high): ").strip().lower()
weather = input("Enter weather (clear/rainy/foggy): ").strip().lower()
time_of_day = input("Enter time of day (morning/afternoon/evening/night): ").strip().lower()
road_type = input("Enter road type (highway/city/rural): ").strip().lower()

# Put inputs into DataFrame
user_input = pd.DataFrame([{
    "distance_km": distance_km,
    "traffic_level": traffic_level,
    "weather": weather,
    "time_of_day": time_of_day,
    "road_type": road_type
}])

# Predict
prediction = pipeline.predict(user_input)[0]

print("\nPredicted Route Metrics:")
print(f"Travel Time (min): {prediction[0]:.2f}")
print(f"Fuel Cost: {prediction[1]:.2f}")
print(f"Scenic Score: {prediction[2]:.2f}")
print(f"Safety Score: {prediction[3]:.2f}")

