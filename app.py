import streamlit as st
import pandas as pd
from agents.orchestrator import orchestrate_response
from utils.db_utils import init_db, log_interaction

# Initialize SQLite database
init_db()

st.title("🌾 AgriGPT - Sustainable Farming Assistant")

# Load farmer dataset
try:
    df = pd.read_csv("data/farmer_advisor_dataset.csv")
    if df.empty or "Name" not in df.columns:
        st.error("⚠️ Farmer dataset is empty or invalid.")
        st.stop()
except FileNotFoundError:
    st.error("❌ Could not find 'farmer_advisor_dataset.csv'. Make sure it exists in the /data folder.")
    st.stop()

# Dropdown for farmer selection
selected_name = st.selectbox("Select Farmer", df["Name"].unique())

# Extract full context for selected farmer
try:
    selected_farmer = df[df["Name"] == selected_name].iloc[0].to_dict()
except Exception as e:
    st.error(f"⚠️ Error selecting farmer: {e}")
    st.stop()

# Show selected data
st.write("📋 Selected Farmer Details:", selected_farmer)

# Run orchestration on click
if st.button("Generate Farming Advice"):
    try:
        result = orchestrate_response(farmer_context=selected_farmer)

        # Display agent responses
        st.subheader("👨‍🌾 Farmer Context")
        st.json(result.get("Farmer Info", {}))

        st.subheader("🌦️ Weather Forecast")
        st.json(result.get("Weather Forecast", {}))

        st.subheader("🌱 Expert Agro Advice")
        st.json(result.get("Expert Advice", {}))

        st.subheader("📈 Market Trends")
        st.json(result.get("Market Trends", {}))

        st.subheader("🧠 Final AI Recommendation")
        st.success(result.get("Final Advice", "No advice returned by LLM."))

        # Log result in SQLite
        log_interaction(
            result["Farmer Info"],
            result["Weather Forecast"],
            result["Expert Advice"],
            result["Market Trends"]
        )

    except Exception as e:
        st.error(f"🚨 An error occurred while generating advice: {e}")
