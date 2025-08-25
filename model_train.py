import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error
import joblib

# Load dataset
df = pd.read_csv("synthetic_routes_dataset.csv")

# Features and Targets
X = df[["distance_km", "traffic_level", "weather", "time_of_day", "road_type"]]
y = df[["travel_time_min", "fuel_cost", "scenic_score", "safety_score"]]

# One-hot encode categorical features
X = pd.get_dummies(X)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = RandomForestRegressor(n_estimators=200, random_state=42)
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Evaluation
mae = mean_absolute_error(y_test, y_pred, multioutput="raw_values")
rmse = np.sqrt(mean_squared_error(y_test, y_pred, multioutput="raw_values"))

print("\nModel Evaluation:")
for i, col in enumerate(y.columns):
    print(f"{col} -> MAE: {mae[i]:.2f}, RMSE: {rmse[i]:.2f}")

# Save model
joblib.dump(model, "route_model.pkl")
print("\n✅ Model saved as route_model.pkl")
