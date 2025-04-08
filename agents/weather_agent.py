# agents/weather_agent.py

def get_weather_forecast(location="Unknown"):
    # Mock weather info – replace with real API later
    sample_weather_data = {
        "Tamil Nadu": {
            "temperature": "32°C",
            "humidity": "68%",
            "rain_chance": "40%",
            "advice": "Slight chance of rain, consider irrigation delay."
        },
        "Punjab": {
            "temperature": "25°C",
            "humidity": "50%",
            "rain_chance": "10%",
            "advice": "No rain expected, irrigation recommended."
        },
        "Unknown": {
            "temperature": "N/A",
            "humidity": "N/A",
            "rain_chance": "N/A",
            "advice": "Location unknown, unable to fetch weather."
        }
    }

    return sample_weather_data.get(location, sample_weather_data["Unknown"])

def get_weather_forecast(region=None, season=None):
    # Dummy weather logic (replace with API/scraped logic later)
    return {
        "Temperature": "25°C - 30°C",
        "Rainfall": "Moderate",
        "Condition": f"Sunny with light showers expected in {region} during {season}"
    }
