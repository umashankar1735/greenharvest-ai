from agents.weather_agent import get_weather_forecast
from agents.expert_agent import get_agro_advice
from agents.market_agent import get_market_insights
from utils.llm_utils import generate_llm_advice

def orchestrate_response(farmer_context):
    # Get weather info
    weather_info = get_weather_forecast(
        region=farmer_context.get("Location", "Unknown"),
        season=farmer_context.get("Season", "Rabi")
    )

    # Get agro advice
    agro_info = get_agro_advice(
        crop=farmer_context.get("Crop", "Wheat"),
        soil_type=farmer_context.get("SoilType", "Loamy"),
        irrigation=farmer_context.get("Irrigation", "Drip"),
        season=farmer_context.get("Season", "Rabi")
    )

    # Get market insights
    market_info = get_market_insights(
        crop=farmer_context.get("Crop", "Wheat"),
        region=farmer_context.get("Location", "Unknown")
    )

    # Prepare prompt for OpenAI
    prompt = f"""
Farmer Details:
- Name: {farmer_context.get('Name', 'Unknown')}
- Crop: {farmer_context.get('Crop', 'Unknown')}
- Location: {farmer_context.get('Location', 'Unknown')}
- Soil Type: {farmer_context.get('SoilType', 'Unknown')}
- Irrigation: {farmer_context.get('Irrigation', 'Unknown')}
- Season: {farmer_context.get('Season', 'Unknown')}

Weather Forecast:
{weather_info}

Expert Advice:
{agro_info}

Market Trends:
{market_info}

Based on the above information, please provide:
1. Personalized farming recommendations
2. Potential risks to watch for
3. Suggested actions for the current season
4. Market strategy advice
"""

    # Get response from OpenAI
    response = generate_llm_advice(prompt)

    return {
        "Farmer Info": farmer_context,
        "Weather Forecast": weather_info,
        "Expert Advice": agro_info,
        "Market Trends": market_info,
        "LLM Response": response
    }
