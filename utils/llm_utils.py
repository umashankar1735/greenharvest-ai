import streamlit as st  # <-- Add this at the top
from groq import Groq

def generate_llm_advice(prompt):
    try:
        client = Groq(api_key=st.secrets["GROQ_API_KEY"])
        response = client.chat.completions.create(
            model="mixtral-8x7b-32768",
            messages=[
                {"role": "system", "content": "You are AgriGPT..."},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"""🌾 AgriGPT Fallback Advice:
1. Monitor soil moisture daily
2. Check local weather forecasts
3. Contact agriculture extension office
[Technical Error: {str(e)}]"""
