from fastapi import FastAPI
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestRegressor

app = FastAPI()

# dummy model
np.random.seed(42)

n = 1000

data = pd.DataFrame({
    "floor_area": np.random.randint(500, 5000, n),
    "occupancy": np.random.randint(5, 200, n),
    "temperature": np.random.randint(10, 40, n),
})

data["energy_usage"] = (
    data["floor_area"] * 0.5 +
    data["occupancy"] * 10 +
    data["temperature"] * 20
)

X = data[["floor_area", "occupancy", "temperature"]]
y = data["energy_usage"]

model = RandomForestRegressor()
model.fit(X, y)

@app.get("/")
def home():
    return {"message": "API Working 🚀"}

@app.post("/predict")
def predict(floor_area: float, occupancy: int, temperature: float):

    input_data = np.array([[floor_area, occupancy, temperature]])
    prediction = model.predict(input_data)[0]

    return {
        "energy": float(prediction)
    }