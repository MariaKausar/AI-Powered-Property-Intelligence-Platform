from fastapi import FastAPI
import numpy as np
import pandas as pd
import random
from sklearn.ensemble import RandomForestRegressor

app = FastAPI()

# -----------------------------
# DATA GENERATION
# -----------------------------
np.random.seed(42)
n = 1000

data = pd.DataFrame({
    "floor_area": np.random.randint(500, 5000, n),
    "occupancy": np.random.randint(5, 200, n),
    "temperature": np.random.randint(10, 40, n),
    "building_age": np.random.randint(1, 50, n),
})

# Target variable (energy usage)
data["energy_usage"] = (
    data["floor_area"] * 0.5 +
    data["occupancy"] * 10 +
    data["temperature"] * 20 -
    data["building_age"] * 5
)

# Extra features (for realism)
data["energy_cost"] = data["energy_usage"] * 0.25
data["epc_rating"] = [random.choice(["A","B","C","D","E","F","G"]) for _ in range(n)]

# -----------------------------
# MODEL TRAINING
# -----------------------------
X = data[["floor_area", "occupancy", "temperature", "building_age"]]
y = data["energy_usage"]

model = RandomForestRegressor()
model.fit(X, y)

# -----------------------------
# ROUTES
# -----------------------------
@app.get("/")
def home():
    return {"message": "Smart Energy API Working 🚀"}

@app.post("/predict")
def predict(
    floor_area: float,
    occupancy: int,
    temperature: float,
    building_age: int
):

    # ML prediction
    input_data = np.array([[floor_area, occupancy, temperature, building_age]])
    prediction = model.predict(input_data)[0]

    # -----------------------------
    # BUSINESS LOGIC (KTP LEVEL 🔥)
    # -----------------------------
    energy = float(prediction)
    cost = energy * 0.25

    # Random EPC rating (simulating real-world data)
    epc = random.choice(["A","B","C","D","E","F","G"])

    # MEES compliance
    if epc in ["F", "G"]:
        mees_status = "Non-Compliant"
    else:
        mees_status = "Compliant"

    # Efficiency scoring (data fusion idea)
    efficiency_score = (
        floor_area * 0.2 +
        occupancy * 0.3 +
        temperature * 0.1 +
        energy * 0.4
    )

    if efficiency_score > 2500:
        efficiency = "Inefficient"
    else:
        efficiency = "Efficient"

    # -----------------------------
    # RESPONSE
    # -----------------------------
    return {
        "energy": energy,
        "cost": cost,
        "epc_rating": epc,
        "mees_status": mees_status,
        "efficiency": efficiency
    }