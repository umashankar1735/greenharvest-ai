# agents/market_agent.py
import pandas as pd
import os

def get_market_insights(crop, region):
    file_path = os.path.join("data", "market_researcher_dataset.csv")
    try:
        df = pd.read_csv(file_path)
        match = df[(df["Crop"].str.lower() == crop.lower()) &
                   (df["Region"].str.lower() == region.lower())]
        if not match.empty:
            record = match.iloc[0]
            return {
                "Market Price": f"₹{record['MarketPrice']} per quintal",
                "Demand Level": record["DemandLevel"],
                "Recommendation": record["Recommendation"]
            }
        else:
            return {
                "Market Price": "Not found",
                "Demand Level": "Unknown",
                "Recommendation": "Check local mandi data."
            }
    except Exception as e:
        return {
            "Market Price": None,
            "Demand Level": None,
            "Recommendation": "Market data fetch failed. Try again."
        }
