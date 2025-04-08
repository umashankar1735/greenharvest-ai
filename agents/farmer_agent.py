# agents/farmer_agent.py

import pandas as pd
import os

def get_farmer_context():
    # Load farmer dataset
    data_path = os.path.join("data", "farmer_advisor_dataset.csv")
    df = pd.read_csv(data_path)

    # For now, pick the first row as sample data
    farmer = df.iloc[0]

    return {
        "name": farmer.get("Name", "Farmer"),
        "location": farmer.get("Location", "Unknown"),
        "crop": farmer.get("Crop", "Wheat"),
        "soil_type": farmer.get("SoilType", "Loamy"),
        "season": farmer.get("Season", "Rabi"),
        "irrigation": farmer.get("Irrigation", "Drip")
    }
