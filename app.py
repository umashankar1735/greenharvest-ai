import streamlit as st
import pandas as pd
from agents.orchestrator import orchestrate_response
import openai

st.title("🌾 AgriGPT - Sustainable Farming Assistant")

# Initialize OpenAI (API key should be in Streamlit secrets)
openai.api_key = st.secrets["OPENAI_API_KEY"]

# Load dataset
try:
    df = pd.read_csv("data/farmer_advisor_dataset.csv")
    if df.empty or "Name" not in df.columns:
        st.error("⚠️ Farmer dataset is empty or invalid.")
        st.stop()
except FileNotFoundError:
    st.error("❌ Could not find 'farmer_advisor_dataset.csv'. Make sure it exists in the /data folder.")
    st.stop()

selected_name = st.selectbox("Select Farmer", df["Name"].unique())

try:
    selected_farmer = df[df["Name"] == selected_name].iloc[0].to_dict()
except Exception as e:
    st.error(f"⚠️ Error selecting farmer: {e}")
    st.stop()

st.write("📋 Selected Farmer Details:", selected_farmer)

if st.button("Generate Farming Advice"):
    with st.spinner("Generating advice using OpenAI..."):
        result = orchestrate_response(farmer_context=selected_farmer)

    st.subheader("👨‍🌾 Farmer Context")
    st.json(result.get("Farmer Info", {}))

    st.subheader("🌦️ Weather Forecast")
    st.json(result.get("Weather Forecast", {}))

    st.subheader("🌱 Expert Agro Advice")
    st.json(result.get("Expert Advice", {}))

    st.subheader("📈 Market Trends")
    st.json(result.get("Market Trends", {}))
    
    st.subheader("🤖 AI Recommendations")
    st.write(result.get("LLM Response", ""))
