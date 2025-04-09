from openai import OpenAI

def generate_llm_advice(prompt, model="gpt-3.5-turbo"):
    try:
        client = OpenAI()  # Automatically uses OPENAI_API_KEY from st.secrets
        
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": "You are AgriGPT, an expert agricultural assistant."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=500
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"[OpenAI Error] {str(e)}"
