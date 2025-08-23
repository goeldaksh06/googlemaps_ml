import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.multioutput import MultiOutputClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import mean_absolute_error, mean_squared_error
import joblib


n_samples = 5000

data = {
    "distance_km": np.random.randint(1, 50, n_samples),
    "traffic_level": np.random.choice(["low", "medium", "high"], n_samples),
    "weather": np.random.choice(["foggy", "sunny", "rainy"], n_samples),
    "time_of_day": np.random.choice(["morning", "afternoon", "evening", "night"], n_samples),
    "road_type": np.random.choice(["highway", "arterial", "local"], n_samples),
}

df = pd.DataFrame(data)

traffic_factor = {"low": 1.0, "medium": 1.5, "high": 2.0}
weather_penalty = {"sunny": 1.0, "rainy": 1.3, "foggy": 1.6}
scenic_bias = {"highway": 0.3, "arterial": 0.5, "local": 0.8}
time_penalty = {"morning": 1.1, "afternoon": 1.3, "evening": 1.2, "night": 0.9}

df["fuel_cost"] = df["distance_km"] * (
    1 + df["traffic_level"].map({"low": 0.1, "medium": 0.2, "high": 0.3}))

df["scenic_score"] = df["road_type"].map(scenic_bias) + np.random.normal(0, 0.1, n_samples)
df["scenic_score"] = df["scenic_score"].clip(0, 1)

df["safety_score"] = (
    1
    - (df["traffic_level"].map({"low": 0.0, "medium": 0.2, "high": 0.4}))
    - (df["weather"].map({"sunny": 0.0, "rainy": 0.2, "foggy": 0.3}))
    + np.random.normal(0, 0.05, n_samples)  
)
df["safety_score"] = df["safety_score"].clip(0, 1)


df["travel_time_min"] = (
    df["distance_km"]
    * df["traffic_level"].map(traffic_factor)
    * df["weather"].map(weather_penalty)
    * df["time_of_day"].map(time_penalty)
    + np.random.normal(0, 5, n_samples)  
)
df["travel_time_min"] = df["travel_time_min"].clip(5, None) 


print(df.head())

print("\n--- Dataset Info ---")
print(df.info())

print("\n--- Summary Statistics ---")
print(df.describe())

print("\n--- Unique Values ---")
for col in ["traffic_level", "weather", "time_of_day", "road_type"]:
    print(f"{col}: {df[col].unique()}")

df.to_csv("synthetic_routes_dataset.csv", index=False)
print("\n✅ Dataset saved as 'synthetic_routes_dataset.csv'")

