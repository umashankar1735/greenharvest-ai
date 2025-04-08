# utils/ollama_llm.py

import subprocess
import json

def generate_llm_advice(prompt, model="llama2"):
    try:
        result = subprocess.run(
            ["ollama", "run", model],
            input=prompt,
            text=True,
            capture_output=True
        )
        return result.stdout.strip()
    except Exception as e:
        return f"[LLM Error] {str(e)}"
