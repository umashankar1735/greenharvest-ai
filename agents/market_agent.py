import pandas as pd
import os

def get_market_insights(crop, region):
    try:
        df = pd.read_csv("data/market_researcher_dataset.csv")
        match = df[(df["Crop"].str.lower() == crop.lower()) & 
                  (df["Region"].str.lower() == region.lower())]
        
        if not match.empty:
            record = match.iloc[0]
            return {
                "Current Price": f"₹{record['MarketPrice']}/quintal",
                "Demand Trend": record["DemandLevel"],
                "Market Advice": record["Recommendation"],
                "Price Trend": "Stable" if record["DemandLevel"] == "Medium" else 
                             "Increasing" if record["DemandLevel"] == "High" else "Decreasing"
            }
        else:
            return {
                "Current Price": "Data not available",
                "Demand Trend": "Unknown",
                "Market Advice": "Check local mandi rates",
                "Price Trend": "Unknown"
            }
    except Exception as e:
        return {
            "Current Price": "Error fetching data",
            "Demand Trend": "Error",
            "Market Advice": "Please try again later",
            "Price Trend": "Error"
        }
