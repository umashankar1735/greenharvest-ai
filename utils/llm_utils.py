# utils/llm_utils.py

import os
from langchain.llms import Ollama

def generate_llm_advice(prompt: str) -> str:
    llm = Ollama(model="llama2:7b-chat", base_url="http://localhost:11434")  # Change model if needed
    return llm.invoke(prompt)
