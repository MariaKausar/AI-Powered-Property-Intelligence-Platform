import streamlit as st
import requests

st.set_page_config(page_title="Energy Intelligence System", layout="centered")

st.title("🏢 AI-Powered Property Intelligence Platform")
st.write("Predict building energy usage, cost, and compliance (MEES)")

# ------------------------
# INPUT FIELDS
# ------------------------
st.subheader("📥 Enter Building Details")

floor_area = st.number_input("Floor Area (sq ft)", min_value=100)
occupancy = st.number_input("Occupancy", min_value=1)
temperature = st.number_input("Temperature (°C)", min_value=0)
building_age = st.number_input("Building Age (years)", min_value=1)

# ------------------------
# BUTTON
# ------------------------
if st.button("🔍 Predict"):

    response = requests.post(
        "http://127.0.0.1:8000/predict",
        params={
            "floor_area": floor_area,
            "occupancy": occupancy,
            "temperature": temperature,
            "building_age": building_age
        }
    )

    result = response.json()

    # ------------------------
    # OUTPUT
    # ------------------------
    st.subheader("📊 Results")

    st.success(f"🔥 Energy Usage: {round(result['energy'], 2)}")
    st.info(f"💰 Energy Cost: £{round(result['cost'], 2)}")
    st.write(f"🏷 EPC Rating: {result['epc_rating']}")

    # ------------------------
    # MEES STATUS
    # ------------------------
    if result["mees_status"] == "Non-Compliant":
        st.error("❌ Building is NOT MEES compliant")
    else:
        st.success("✅ Building is MEES compliant")

    # ------------------------
    # EFFICIENCY
    # ------------------------
    if result["efficiency"] == "Inefficient":
        st.warning("⚠ Inefficient Building – Needs Improvement")
    else:
        st.success("🌱 Energy Efficient Building")
