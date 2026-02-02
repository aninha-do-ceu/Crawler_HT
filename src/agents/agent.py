# ---------------------------------------- #

# Classe para chamada de agentes

# ---------------------------------------- #

import os
from openai import OpenAI

class Agent:
    """
    Base para a chamada do agente de IA
    Métodos:
        get_llm_client
        call_llm
    """

    def __init__(self,
                 model_name: str,
                 temperature: float):
        self.model_name = model_name
        self.temperature = temperature


    def get_llm_client(self):
        client = OpenAI(
            base_url="https://router.huggingface.co/v1",
            api_key=os.environ["HF_TOKEN"],
        )
        return client

    def call_llm(self, client, prompt: str, temperature: float):
        messages = [
            {
                "role": "system",
                "content": "Você é um assistente para extrair links pertinentes de textos."
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
        response_search = client.chat.completions.create(
            model="deepseek-chat",
            messages=messages,
            temperature=temperature
        )
        return response_search.choices[0].message.content
