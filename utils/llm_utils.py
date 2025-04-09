from openai import OpenAI
import streamlit as st

def generate_llm_advice(prompt):
    try:
        # Initialize client with error handling
        client = OpenAI(
            api_key=st.secrets["OPENAI_API_KEY"],  # Updated key will auto-load here
            timeout=10  # Prevents hanging
        )
        
        response = client.chat.completions.create(
            model="gpt-3.5-turbo-0125",  # Newer model version
            messages=[
                {"role": "system", "content": "You are AgriGPT..."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=350  # More efficient usage
        )
        return response.choices[0].message.content
        
    except Exception as e:
        return f"⚠️ Agricultural Insights Unavailable. Technical Details: {str(e)}"
