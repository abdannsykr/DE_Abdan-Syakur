import os
import pandas as pd
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
my_api = os.getenv("NAGA_AI_KEY")
client = OpenAI(
    api_key= my_api,
    base_url='https://api.naga.ac/v1'
    )

def genearate(prompt, model="gpt-3.5-turbo"):
    response = client.chat.completions.create(
        model=model,
        messages=[
            {
                "role": "user",
                "content": prompt}
        ]
    )
    return response.choices[0].message.content

result = genearate("Buatkan saya dataset penjualan")
print(result)