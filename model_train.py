import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
import joblib

# Load dataset
df = pd.read_csv("synthetic_routes_dataset.csv")

# Features and Targets
X = df[["distance_km", "traffic_level", "weather", "time_of_day", "road_type"]]
y = df[["travel_time_min", "fuel_cost", "scenic_score", "safety_score"]]

# Define preprocessing
preprocessor = ColumnTransformer([
    ("cat", OneHotEncoder(handle_unknown="ignore"),
     ["traffic_level", "weather", "time_of_day", "road_type"]),
    ("num", StandardScaler(), ["distance_km"])
])

# Build pipeline (preprocessing + model)
pipeline = Pipeline([
    ("preprocessor", preprocessor),
    ("model", RandomForestRegressor(n_estimators=200, random_state=42))
])

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train pipeline
pipeline.fit(X_train, y_train)

# Predictions
y_pred = pipeline.predict(X_test)

# Evaluation
mae = mean_absolute_error(y_test, y_pred, multioutput="raw_values")
rmse = np.sqrt(mean_squared_error(y_test, y_pred, multioutput="raw_values"))

print("\nModel Evaluation:")
for i, col in enumerate(y.columns):
    print(f"{col} -> MAE: {mae[i]:.2f}, RMSE: {rmse[i]:.2f}")

# Save full pipeline
joblib.dump(pipeline, "route_model.pkl")
print("\n✅ Pipeline (with preprocessing) saved as route_model.pkl")
