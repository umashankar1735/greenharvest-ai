def get_weather_forecast(region="Unknown", season=None):
    # This can be replaced with actual API calls to weather services
    weather_data = {
        "Tamil Nadu": {
            "Temperature": "28-34°C",
            "Humidity": "70-80%",
            "Rainfall": "Moderate to heavy",
            "Forecast": f"Typical {season} season weather with intermittent rains",
            "Advisory": "Prepare for possible waterlogging in low-lying areas"
        },
        "Punjab": {
            "Temperature": "18-28°C",
            "Humidity": "40-60%",
            "Rainfall": "Light to moderate",
            "Forecast": f"Cool {season} season with occasional showers",
            "Advisory": "Monitor for early morning frost warnings"
        },
        "Kerala": {
            "Temperature": "26-32°C",
            "Humidity": "75-85%",
            "Rainfall": "Heavy",
            "Forecast": f"Humid {season} season with frequent rains",
            "Advisory": "Watch for fungal diseases due to high humidity"
        },
        "Unknown": {
            "Temperature": "N/A",
            "Humidity": "N/A",
            "Rainfall": "N/A",
            "Forecast": "Region not specified",
            "Advisory": "Check local weather reports for accurate information"
        }
    }
    
    return weather_data.get(region, weather_data["Unknown"])
