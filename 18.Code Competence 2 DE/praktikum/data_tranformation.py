import os
import pandas as pd
from datetime import datetime
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from firebase_admin import storage  # Tambahkan import untuk akses storage

class DataWarehouseLoader:
    def __init__(self):
        # Inisialisasi Firebase Admin SDK dengan path ke file credential
        cred = credentials.Certificate(r"C:\Users\abdan\Documents\GitHub\DE_Abdan-Syakur\18.Code Competence 2 DE\praktikum\pythonKey.json")
        firebase_admin.initialize_app(cred, {
             "databaseURL": "gs://code-competence2.appspot.com"  # Ganti <nama-proyek> dengan nama proyek Firebase Anda
        })
        self.bucket = storage.bucket()  # Gunakan self.bucket agar dapat diakses di dalam kelas

    def load_data(self, file_path):
        # Membaca file Parquet dari Data Lake
        df = pd.read_parquet(file_path)
        return df

    def transform_data(self, df_transactions, df_tickets, df_events, df_customer_feedback):
        # Implementasi transformasi data seperti yang Anda inginkan
        # Misalnya, menggabungkan DataFrame, melakukan penghitungan, dll.
        # Contoh sederhana:
        merged_df = pd.merge(df_transactions, df_tickets, on='ticket_id', how='inner')
        merged_df = pd.merge(merged_df, df_events, on='event_id', how='inner')

        # Menghitung jumlah tiket terjual per acara
        tickets_sold_per_event = merged_df.groupby('event_id')['quantity'].sum().reset_index()
        tickets_sold_per_event.columns = ['event_id', 'tickets_sold']

        # Menghitung total pendapatan dari setiap acara
        revenue_per_event = merged_df.groupby('event_id')['total_amount'].sum().reset_index()

        # Analisis rata-rata rating per acara (pastikan 'event_id' ada di df_customer_feedback)
        if 'event_id' in df_customer_feedback.columns:
            avg_rating_per_event = df_customer_feedback.groupby('event_id')['rating'].mean().reset_index()
        else:
            avg_rating_per_event = pd.DataFrame()  # Buat DataFrame kosong jika 'event_id' tidak ada

        return tickets_sold_per_event, revenue_per_event, avg_rating_per_event

    def save_to_warehouse(self, df, node_name):
        # Struktur Folder Berdasarkan DateTime
        current_date = datetime.now().strftime('%Y/%m/%d')

        # Simpan DataFrame ke Firebase Realtime Database
        ref = db.reference(f'{current_date}/{node_name}')
        try:
            ref.set(df.to_dict(orient='records'))
            print(f"Data berhasil disimpan di Firebase Realtime Database: {current_date}/{node_name}")
        except Exception as e:
            print(f"Terjadi kesalahan saat menyimpan data ke Firebase Realtime Database: {e}")

if __name__ == "__main__":
    # Inisialisasi DataWarehouseLoader
    loader = DataWarehouseLoader()

    # Load data dari Data Lake untuk tabel events, customers, tickets, transactions, dan customer_feedback
    events_df = loader.load_data('data_source/events.parquet')
    customers_df = loader.load_data('data_source/customers.parquet')
    tickets_df = loader.load_data('data_source/tickets.parquet')
    transactions_df = loader.load_data('data_source/transactions.parquet')
    customer_feedback_df = loader.load_data('data_source/customer_feedback.parquet')

    # Transformasi data
    tickets_sold, revenue, avg_rating = loader.transform_data(transactions_df, tickets_df, events_df, customer_feedback_df)

    # Simpan hasil transformasi ke Firebase Realtime Database
    loader.save_to_warehouse(tickets_sold, 'tickets_sold_per_event')
    loader.save_to_warehouse(revenue, 'revenue_per_event')
    loader.save_to_warehouse(avg_rating, 'avg_rating_per_event')
