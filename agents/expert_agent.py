# agents/expert_agent.py

def get_agro_advice(crop, soil_type):
    # Static mapping of expert advice for now
    expert_database = {
        "Rice": {
            "Clay": {
                "fertilizer": "Use Urea and Potash with organic compost.",
                "irrigation": "Maintain flooded fields with 3-5 cm water.",
                "advice": "Ideal soil. Watch out for pests like stem borers."
            },
            "Loamy": {
                "fertilizer": "Apply NPK 20:20:0 and green manure.",
                "irrigation": "Irrigate twice a week, keep soil moist.",
                "advice": "Loamy soil is good, ensure proper drainage."
            }
        },
        "Wheat": {
            "Loamy": {
                "fertilizer": "Apply DAP and Zinc Sulfate.",
                "irrigation": "Irrigate at crown root initiation and booting stages.",
                "advice": "Monitor for yellow rust and apply fungicide if needed."
            }
        },
        "Banana": {
            "Sandy": {
                "fertilizer": "Use well-decomposed FYM and potassium nitrate.",
                "irrigation": "Drip irrigation recommended twice daily.",
                "advice": "Support the stem, avoid waterlogging."
            }
        }
    }

    try:
        data = expert_database[crop][soil_type]
    except KeyError:
        data = {
            "fertilizer": "No specific recommendation available.",
            "irrigation": "Use general crop-specific irrigation.",
            "advice": "Monitor local agri bulletin for best practices."
        }

    return data

# agents/expert_agent.py

def get_agro_advice(crop=None, soil_type=None, irrigation=None, season=None):
    # Sample logic (replace with actual dataset analysis)
    return {
        "Recommended Fertilizer": f"Organic compost for {soil_type} soil",
        "Irrigation Advice": f"{irrigation}-based watering every 5 days",
        "Potential Disease Risk": f"Low disease risk for {crop} during {season}"
    }
