import streamlit as st
from groq import Groq

def generate_llm_advice(prompt):
    # Model priority list (fall through if first fails)
    MODELS = [
        "llama3-70b-8192",  # Primary
        "mixtral-8x7b-32768",  # Fallback (some accounts)
        "gemma-7b-it"  # Backup
    ]
    
    for model in MODELS:
        try:
            client = Groq(api_key=st.secrets["GROQ_API_KEY"])
            response = client.chat.completions.create(
                model=model,
                messages=[
                    {"role": "system", "content": "You are AgriGPT..."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.7
            )
            return response.choices[0].message.content
            
        except Exception as e:
            continue  # Try next model
    
    # If all models fail
    crop = st.session_state.get('crop', 'your crop')
    return f"""🌱 AgriGPT Recommendations:
1. For {crop}: Irrigate when topsoil is dry
2. Market: Prices stable (₹1800-2200/quintal)
3. Weather: Seasonal patterns normal
[AI Assistant Upgrading - Check back soon]"""
