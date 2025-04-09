# main.py

from agents.farmer_agent import get_farmer_context
from agents.weather_agent import get_weather_forecast
from agents.expert_agent import get_agro_advice
from agents.market_agent import get_market_insights
from utils.db_utils import init_db, log_interaction


def run_agriGPT():
    print("🌾 Welcome to AgriGPT - Sustainable Farming Advisor\n")

    # Step 1: Collect farmer input
    farmer_context = get_farmer_context()
    print("👩‍🌾 Farmer Context Retrieved:")
    for key, value in farmer_context.items():
        print(f"  {key}: {value}")

    # Step 2: Get weather info based on location
    print("\n🌦️ Weather Forecast:")
    weather = get_weather_forecast(farmer_context["Location"])
    for key, value in weather.items():
        print(f"  {key}: {value}")

     # Step 3: Get agro advice
    print("\n🌿 Agro Expert Advice:")
    expert_advice = get_agro_advice(
        crop=farmer_context["Crop"],
        soil_type=farmer_context["Soil_Type"]
    )
    for key, value in expert_advice.items():
        print(f"  {key}: {value}")

    
    # Step 4: Get market insights
    print("\n📈 Market Intelligence:")
    market_info = get_market_insights(
        crop=farmer_context["Crop"],
        region=farmer_context["Location"]
    )
    for key, value in market_info.items():
        print(f"  {key}: {value}")

    init_db()  # Initialize DB once

if __name__ == "__main__":
    run_agriGPT()

# main.py

from agents.orchestrator import orchestrate_response

if __name__ == "__main__":
    print("🌾 Welcome to AgriGPT - Sustainable Farming Advisor\n")
    final_report = orchestrate_response()
    print(final_report)

log_interaction(result["Farmer Info"], result["Weather Forecast"], result["Expert Advice"], result["Market Trends"])




