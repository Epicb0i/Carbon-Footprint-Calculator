import streamlit as st

# App config
st.set_page_config(page_title="India Carbon Footprint Calculator", layout="centered")

st.title("India Based Carbon Footprint Calculator")
st.markdown("Estimate your **annual CO2e emissions** in metric tons. This tool uses Indian emission factors (e.g., electricity in Units).")

st.divider()

# --- ENERGY SECTION ---
st.header("🔌 Energy Use")

electricity_units = st.number_input("Monthly Electricity Usage (in Units)", min_value=0.0, step=1.0)
lpg_kg = st.number_input("Monthly LPG Usage (in kg)", min_value=0.0, step=0.5)

# --- PERSONAL VEHICLES ---
st.header("🚗 Personal Vehicles")

car_km = st.number_input("Car Travel Distance (km/year)", min_value=0.0)
car_eff = st.number_input("Car Fuel Efficiency (L/100km)", min_value=0.0)

bike_km = st.number_input("Motorbike Travel Distance (km/year)", min_value=0.0)
bike_eff = st.number_input("Motorbike Fuel Efficiency (L/100km)", min_value=0.0)

# --- FLIGHTS ---
st.header("✈️ Flights")

short_flights = st.number_input("Short Return Flights (Domestic)", min_value=0, step=1)
long_flights = st.number_input("Long Return Flights (International)", min_value=0, step=1)

# --- PUBLIC TRANSPORT ---
st.header("🚌 Public Transport (km/year)")

bus_km = st.number_input("Bus", min_value=0.0)
train_km = st.number_input("Train", min_value=0.0)
tram_km = st.number_input("Tram/Subway", min_value=0.0)
taxi_km = st.number_input("Taxi", min_value=0.0)

# --- EMISSION FACTORS ---
ef = {
    "electricity": 1.1405,      # kg CO2e per Unit
    "lpg": 2.983,               # kg CO2e per kg
    "petrol": 2.31,             # kg CO2e per litre
    "flight_short": 0.15 * 1000,  # kg per return flight
    "flight_long": 1.6 * 1000,
    "bus": 0.105,
    "train": 0.041,
    "tram": 0.035,
    "taxi": 0.175
}

# --- CALCULATIONS ---
electricity_annual = electricity_units * 12 * ef["electricity"]
lpg_annual = lpg_kg * 12 * ef["lpg"]
car_annual = (car_km / 100) * car_eff * ef["petrol"]
bike_annual = (bike_km / 100) * bike_eff * ef["petrol"]
flights_annual = (short_flights * ef["flight_short"] + long_flights * ef["flight_long"])
public_transport_annual = (bus_km * ef["bus"] + train_km * ef["train"] +
                           tram_km * ef["tram"] + taxi_km * ef["taxi"])

total_kg = electricity_annual + lpg_annual + car_annual + bike_annual + flights_annual + public_transport_annual
total_tons = total_kg / 1000

# --- OUTPUT ---
st.divider()
st.subheader("🌍 Your Estimated Annual Carbon Footprint")

st.metric(label="Total CO2e", value=f"{total_tons:.2f} metric tons/year")

with st.expander("🔍 See Detailed Breakdown"):
    st.write(f"**Electricity:** {electricity_annual:.2f} kg CO2e")
    st.write(f"**LPG:** {lpg_annual:.2f} kg CO2e")
    st.write(f"**Car:** {car_annual:.2f} kg CO2e")
    st.write(f"**Motorbike:** {bike_annual:.2f} kg CO2e")
    st.write(f"**Flights:** {flights_annual:.2f} kg CO2e")
    st.write(f"**Public Transport:** {public_transport_annual:.2f} kg CO2e")

st.caption("Built with ❤️ using Streamlit • Based on Indian emission standards (2025)")
