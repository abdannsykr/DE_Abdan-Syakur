from datetime import datetime, timedelta
import random
from airflow import DAG
from airflow.operators.python import PythonOperator

def generate_random_numbers():
  """Menghasilkan daftar 25 bilangan acak antara 1 dan 50."""
  angka_acak = [random.randint(1, 50) for _ in range(25)]
  return angka_acak

def calculate_sum(ti):
  """Menghitung jumlah dari daftar bilangan acak."""
  angka_acak = ti.xcom_pull(task_ids="generate_random_numbers")

  # Validasi isi list angka_acak
  if not all(isinstance(angka, int) and angka.isnumeric() for angka in angka_acak):
      print("Angka tidak valid ditemukan dalam daftar bilangan acak. Melewati task.")
      return

  jumlah_angka = sum(angka_acak)

  # Validasi tipe data jumlah_angka
  if not isinstance(jumlah_angka, int):
      print("Tipe data jumlah tidak valid: {}. Melewati task.".format(jumlah_angka))
      return

  ti.xcom_push(key="sum_result", value=jumlah_angka)

def check_even_odd(ti):
  """Memeriksa apakah jumlah bilangan acak genap atau ganjil."""
  jumlah = ti.xcom_pull(task_ids="calculate_sum", key="sum_result")

  if jumlah is None:
      print("Gagal mengambil jumlah dari XCom. Melewati task.")
      return

  hasil = "Genap" if jumlah % 2 == 0 else "Ganjil"
  print(f"Jumlah: {jumlah}")
  print(f"Hasil: {hasil}")

default_args = {
  "owner": "abdan",
  "retries": 5,
  "retry_delay": timedelta(minutes=5),
}

with DAG(
  dag_id="prioritas1_no2",
  default_args=default_args,
  description="DAG untuk menghasilkan bilangan acak, menghitung jumlah dan menentukan genap atau ganjil",
  schedule_interval="@daily",
  start_date=datetime(2024, 4, 9),
  catchup=False,
) as dag:

  generate_random_task = PythonOperator(
    task_id="generate_random_numbers",
    python_callable=generate_random_numbers,
  )

  calculate_sum_task = PythonOperator(
    task_id="calculate_sum",
    python_callable=calculate_sum,
    provide_context=True,
  )

  check_even_odd_task = PythonOperator(
    task_id="check_even_odd",
    python_callable=check_even_odd,
  )

  generate_random_task >> calculate_sum_task >> check_even_odd_task
