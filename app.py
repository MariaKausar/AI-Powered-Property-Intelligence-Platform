import streamlit as st
import requests

st.title("🏢 Smart Energy Intelligence System")

floor_area = st.number_input("Floor Area", min_value=100)
occupancy = st.number_input("Occupancy", min_value=1)
temperature = st.number_input("Temperature", min_value=0)

if st.button("Predict Energy Usage"):

    response = requests.post(
        "http://127.0.0.1:8000/predict",
        params={
            "floor_area": floor_area,
            "occupancy": occupancy,
            "temperature": temperature
        }
    )

    result = response.json()

    st.success(f"🔥 Predicted Energy Usage: {result['energy']}")

    if result["energy"] > 2000:
        st.error("⚠ High Energy Consumption Building")
    else:
        st.success("✅ Efficient Building")