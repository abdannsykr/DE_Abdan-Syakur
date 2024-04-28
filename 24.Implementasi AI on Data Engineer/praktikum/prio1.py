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

prompt = """Buatkan dataset penjualan yang mencakup informasi penting Tanggal,Jumlah_Penjualan,Harga,Kategori_Produk. 
            Maka buatlah Dataset yang Fokus terhadap pada analisis tren penjualan, segmentasi pelanggan, dan prediksi penjualan."""

def generate(prompt, model="gpt-3.5-turbo"):
    result = generate(prompt, model)
    return result

penjualan_dataset = generate(prompt)

df_penjualan = pd.DataFrame({"penjualan_Dataset": [penjualan_dataset]})

df_penjualan.to_csv("penjualan_dataset.csv", index=False)
