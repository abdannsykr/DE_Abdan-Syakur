## Rangkuman Workflow Orchestration with Airflow

### Apache Airflow Introduction
Workflow adalah sekumpulan tugas yang terhubung satu sama lain untuk mencapai tujuan tertentu.

Task adalah sebuah tugas yang diselsaikan dari sebuah workflow.

Operator adalah sebuah komponen yang digunakan untuk menjalankan sebuah task.

DAG adalah singkatan dari Directed Acylic Graph. DAG adalah sebuah graf yang digunakan untuk menggambarkan sebuah workflow.

Apache Airflow adalah sebuah tools yang dapat digunakan untuk mengelola workflow.

### Using XCOM in DAG
XCOM adalah sebuatan dari cross communication yang memungkinkan antar task dapat bertukar atau mengirim data.

### Taskflow DAG
Taskflow dapat digunakan untuk membuat sebuah data pipeline di Airflow.

### Create DAG with Custom Image
    - DAG dijalankan dengan menggunakan library Python yang sudah built-in sehingga jika membutuhkan library eksternal tambahan maka perlu menyiapkan Docker Image yang dibuat secara custom.
    - Custom Image dapat digunakan untuk menjalankan sebuah DAG yang membutuhkan dependensi / library tambahan yang belum tersedia secaara default di python.
    - Teknik ini dapat digunakan jika aplikasi Airflow dijalankan dengan Docker Compose.

### Send Email
Mengirim Email di DAG
    - Pada Apache Airflow terdapat fitur untuk mengirim sebuah email
    - Email bisa dikirim jika DAG mengalami kegagalan atau berhasil dijalankan.
    - Konfigurasi email bisa disesuaikan dengan SMTP yang digunakan.
    - Bisa juga menggunakan SMTP lokal seperti MailHog sebagai percobaan.
