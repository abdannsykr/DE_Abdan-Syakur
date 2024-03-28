## Rangkuman Data Warehouse and Data Lake

### Data Warehouse
Data Warehouse adalah sistem yang menggabungkan data dari sumber yang berbeda ke dalam penyimpanan data pusat, tunggal, dan konsisten untuk mendukung analisis data, penggalian data, kecerdasan buatan (AI), dan pembelajaran mesin. 

### Data Warehouse vs Data Lake
Data lake cenderung mencakup data mentah dalam jumlah besar, yang tujuannya mungkin belum ditentukan. Sedangkan data warehouse adalah repositori untuk data terstruktur yang telah difilter dan diproses untuk tujuan tertentu.

Data lake adalah kumpulan besar data mentah yang tujuan penggunaannya mungkin belum ditetapkan.
Data warehouse adalah penyimpanan untuk data terstruktur yang telah difilter dan diproses untuk tujuan tertentu.

### Data Lakehouse
Data lakehouse adalah arsitektur manajemen data terbuka yang menggabungkan fleksibilitas dan efisiensi biaya dari data lake dengan manajemen data dan fitur struktur dari data warehouse, semuanya dalam satu platform data. 

### What is Citus?
Citus adalah ekstensi open source untuk PostgreSQL yang mengubah PostgreSQL menjadi database terdistribusi. Citus menggunakan tabel terdistribusi, tabel referensi, dan mesin kueri SQL terdistribusi untuk memungkinkan skalabilitas horizontal dan kinerja tinggi untuk kueri SQL kompleks pada kumpulan data besar.

### Citus Advantages
Tabel terdistribusi dipecah-pecah di seluruh kluster node PostgreSQL untuk menggabungkan kapasitas CPU, memori, penyimpanan, dan I/O mereka.

Tabel referensi direplikasi ke semua node untuk gabungan dan kunci asing dari tabel terdistribusi dan kinerja baca maksimum.

Mesin kueri terdistribusi merutekan dan memparalelkan operasi SELECT, DML, dan lainnya pada tabel terdistribusi di seluruh kluster.

Penyimpanan kolumnar mengkompres data, mempercepat pemindaian, dan mendukung proyeksi cepat, baik pada tabel biasa maupun terdistribusi.

Kueri dari node mana pun memungkinkan Anda untuk memanfaatkan kapasitas penuh kluster Anda untuk kueri terdistribusi.

### Replication vs Sharding
Replikasi
    - Data yang sama disalin di antara beberapa node

    - Digunakan untuk backup/ketersediaan tinggi

Sharding
    - Data dipotong menjadi beberapa bagian dan didistribusikan di antara beberapa node

    - Digunakan untuk pemrosesan/penyimpanan terdistribusi

    - Anda dapat menyimpan data lebih besar dari kapasitas node

### SCHEMA
Star Schema
    - Fact Table biasanya berisi angka dan referensi ke tabel dimensi
    - Tabel Dimensi (Dimension Tables)

Snowflake Schema
    - Tabel Fakta (Fact Table)
    - Dimension Tables (dinormalisasi) 
    - penyimpanan efisien

One Big Table (OBT)
    - Tidak ada normalisasi sama sekali
    - Performa bagus, banyak redundansi

### Colocation
Tanpa Colocation:
    - Data acara dan halaman tenant mungkin tersebar di beberapa shard.
    - Shard adalah partisi horizontal dari database

Dengan Colocation:
    - Semua data untuk tenant disimpan bersama pada node yang sama
    - Ini dapat meningkatkan efisiensi kueri untuk operasi gabungan pada data tenant

### Google Cloud Platform
Platform cloud menyediakan beberapa layanan dan infrastruktur, sehingga perusahaan tidak perlu menyediakan semuanya sendiri.
beberapa platform cloud terkenal :
    - GCP
    - AWS
    - Azure
    - Ali cloud

