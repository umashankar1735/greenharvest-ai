# agents/orchestrator.py

from agents.farmer_agent import get_farmer_context
from agents.weather_agent import get_weather_forecast
from agents.expert_agent import get_agro_advice
from agents.market_agent import get_market_insights
from utils.llm_utils import generate_llm_advice


def orchestrate_response(farmer_context=None):
    if farmer_context is None:
        farmer_context = get_farmer_context()

    # Step 1: Gather all agent data
    weather_info = get_weather_forecast(
        region=farmer_context.get("Location", "Unknown"),
        season=farmer_context.get("Season", "Rabi")
    )

    agro_info = get_agro_advice(
        crop=farmer_context.get("Crop", "Wheat"),
        soil_type=farmer_context.get("SoilType", "Loamy"),
        irrigation=farmer_context.get("Irrigation", "Drip"),
        season=farmer_context.get("Season", "Rabi")
    )

    market_info = get_market_insights(
        crop=farmer_context.get("Crop", "Wheat"),
        region=farmer_context.get("Location", "Unknown")
    )

    # Step 2: Create LLM prompt (no FAISS context)
    prompt = f"""
You are AgriGPT, a helpful and intelligent farming assistant.

Farmer Details:
- Crop: {farmer_context['Crop']}
- Location: {farmer_context['Location']}
- Soil Type: {farmer_context['SoilType']}
- Season: {farmer_context['Season']}
- Irrigation: {farmer_context['Irrigation']}

Weather Forecast:
{weather_info}

Expert Agro Advice:
{agro_info}

Market Trends:
{market_info}

👉 Based on the above information, provide a 3-paragraph farming recommendation in simple, practical language.
""".strip()

    # Step 3: Query the LLM
    final_advice = generate_llm_advice(prompt)

    return {
        "Farmer Info": farmer_context,
        "Weather Forecast": weather_info,
        "Expert Advice": agro_info,
        "Market Trends": market_info,
        "Final Advice": final_advice
    }
