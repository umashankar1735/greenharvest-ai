def get_agro_advice(crop=None, soil_type=None, irrigation=None, season=None):
    # Database of expert recommendations
    advice_db = {
        "Rice": {
            "Clay": {
                "Fertilizer": "Apply 60 kg N, 30 kg P2O5, and 30 kg K2O per acre",
                "Water Management": "Maintain 2-5 cm standing water",
                "Pest Control": "Monitor for stem borer and leaf folder",
                "General Advice": "Transplant 25-30 day old seedlings"
            },
            "Loamy": {
                "Fertilizer": "Apply 80 kg N, 40 kg P2O5, and 40 kg K2O per acre",
                "Water Management": "Alternate wetting and drying",
                "Pest Control": "Watch for brown plant hopper",
                "General Advice": "Use certified seeds for better yield"
            }
        },
        "Wheat": {
            "Loamy": {
                "Fertilizer": "Apply 120 kg N, 60 kg P2O5, and 40 kg K2O per acre",
                "Water Management": "4-5 irrigations at critical stages",
                "Pest Control": "Monitor for yellow rust and aphids",
                "General Advice": "Timely sowing is crucial for good yield"
            }
        },
        "Banana": {
            "Sandy": {
                "Fertilizer": "Apply 200 g N, 60 g P2O5, and 300 g K2O per plant",
                "Water Management": "Drip irrigation recommended",
                "Pest Control": "Watch for sigatoka leaf spot",
                "General Advice": "Provide proper support to plants"
            }
        }
    }
    
    try:
        return advice_db[crop][soil_type]
    except KeyError:
        return {
            "Fertilizer": "General NPK application recommended",
            "Water Management": "Maintain adequate soil moisture",
            "Pest Control": "Regular field monitoring advised",
            "General Advice": "Consult local agriculture officer"
        }
