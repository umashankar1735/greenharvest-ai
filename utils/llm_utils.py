from groq import Groq  # Replace OpenAI import

def generate_llm_advice(prompt):
    try:
        client = Groq(api_key=st.secrets["GROQ_API_KEY"])  # New key
        response = client.chat.completions.create(
            model="mixtral-8x7b-32768",  # Groq's free model
            messages=[
                {"role": "system", "content": "You are AgriGPT..."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"🌾 Fallback Advice: Monitor soil moisture. [Error: {e}]"
