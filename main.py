import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error

# -------------------------
# 1. CREATE DATASET
# -------------------------
np.random.seed(42)

n = 2000

data = pd.DataFrame({
    "floor_area": np.random.randint(500, 5000, n),
    "occupancy": np.random.randint(5, 200, n),
    "temperature": np.random.randint(10, 40, n),
})

# synthetic energy formula
data["energy_usage"] = (
    data["floor_area"] * 0.5 +
    data["occupancy"] * 10 +
    data["temperature"] * 20 +
    np.random.normal(0, 50, n)
)

print("Dataset Created:")
print(data.head())

# -------------------------
# 2. SPLIT DATA
# -------------------------
X = data[["floor_area", "occupancy", "temperature"]]
y = data["energy_usage"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# -------------------------
# 3. TRAIN MODEL
# -------------------------
model = RandomForestRegressor()
model.fit(X_train, y_train)

# -------------------------
# 4. PREDICT
# -------------------------
predictions = model.predict(X_test)

rmse = np.sqrt(mean_squared_error(y_test, predictions))

print("\nModel Training Completed")
print("RMSE:", rmse)