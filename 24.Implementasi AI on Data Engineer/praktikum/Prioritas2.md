1. Membuat Database
    
-   Buatkan tabel dengan atribut kurang lebih memiliki tanggal transaksi, jumlah penjualan, harga, kategori produk, dan lainnya:


    CREATE TABLE Penjualan (

        id_transaksi SERIAL PRIMARY KEY,

        tanggal_transaksi DATE NOT NULL,

        jumlah_penjualan INT NOT NULL,

        harga DECIMAL(10, 2) NOT NULL,

        kategori_produk VARCHAR(50) NOT NULL,

        nama_produk VARCHAR(100),

        metode_pembayaran VARCHAR(50),

        lokasi_penjualan VARCHAR(100)

    );

Tabel diatas memiliki beberapa kolom yang mencakup informasi penting tentang penjualan:

1. id_transaksi: 

Sebuah nomor identifikasi unik untuk setiap transaksi. Ini menggunakan tipe data SERIAL untuk otomatis menghasilkan nilai yang unik untuk setiap transaksi.

2. tanggal_transaksi:

Tanggal ketika transaksi dilakukan. Digunakan tipe data DATE.
jumlah_penjualan: Jumlah barang yang terjual dalam transaksi tersebut. Digunakan tipe data INT.

3. harga: 

Harga barang per unit dalam transaksi tersebut. Digunakan tipe data DECIMAL untuk menangani nilai pecahan.

4. kategori_produk: 

Kategori atau jenis produk yang terjual. Digunakan tipe data VARCHAR.

5. nama_produk: 

Nama produk yang terjual.

6. metode_pembayaran: 

Cara pembayaran yang digunakan dalam transaksi (misalnya tunai, kartu kredit, transfer bank, dll.).

7. lokasi_penjualan: 

Lokasi atau cabang toko tempat transaksi dilakukan.


Generate SQL dengan OpenAI API:

-   Gunakan OpenAI API untuk menghasilkan SQL queries. Misalnya, berikan prompt seperti
"Buatkan SQL query untuk menghitung total penjualan per kategori produk setiap bulan."


    SELECT EXTRACT(YEAR FROM tanggal_transaksi) AS tahun,

        EXTRACT(MONTH FROM tanggal_transaksi) AS bulan,

        kategori_produk,

        SUM(jumlah_penjualan) AS total_penjualan

    FROM Penjualan

    GROUP BY tahun, bulan, kategori_produk

    ORDER BY tahun, bulan, kategori_produk;


-   Catat respons AI dan analisis keakuratan serta relevansi query yang dihasilkan.

Query ini dengan tepat mengatasi permintaan dengan menghitung total penjualan per kategori produk setiap bulan.

Query menggunakan fungsi EXTRACT dengan benar untuk mengekstrak tahun dan bulan dari kolom tanggal_transaksi.

Fungsi SUM digunakan untuk menghitung total penjualan dalam setiap grup.

Klausul GROUP BY dengan benar mengelompokkan data berdasarkan tahun, bulan, dan kategori produk.

Klausul ORDER BY memastikan bahwa hasilnya diurutkan kronologis berdasarkan tahun, bulan, dan kemudian secara alfabetis berdasarkan kategori produk.

Validasi Query SQL:

-   Validasi SQL queries yang dihasilkan menggunakan sistem manajemen database yang ada. Pastikan query berjalan dengan benar dan menghasilkan output yang diharapkan.

Output:

![alt text](https://github.com/abdannsykr/DE_Abdan-Syakur/blob/main/23.Introduction%20AI%20on%20Data%20Engineer/screenshot/input3.jpg)


Implementasi dan Analisis Hasil:

-   Terapkan SQL queries yang telah divalidasi dan dioptimalkan dalam sistem database perusahaan.


    # Membuat database 'Penjualan'
    CREATE DATABASE prio2;

    # Menggunakan database 'Penjualan'
    USE prio2;

    # Membuat tabel 'Penjualan'
    CREATE TABLE Penjualan (
      
        id_transaksi SERIAL PRIMARY KEY,
      
        tanggal_transaksi DATE NOT NULL,
      
        jumlah_penjualan INT NOT NULL,
      
        harga DECIMAL(10, 2) NOT NULL,
      
        kategori_produk VARCHAR(50) NOT NULL,
      
        nama_produk VARCHAR(100),
      
        metode_pembayaran VARCHAR(50),
      
        lokasi_penjualan VARCHAR(100)
    
    );

    # Memasukkan data ke dalam tabel 'Penjualan'
    INSERT INTO Penjualan (tanggal_transaksi, jumlah_penjualan, harga, 
    
    kategori_produk, nama_produk, metode_pembayaran, lokasi_penjualan)
    
    VALUES 
    
    ('2024-04-28', 10, 350000.00, 'Elektronik', 'Smartphone', 'Kartu Kredit', 'Jakarta'),
    
    ('2024-04-28', 10, 50000.00, 'Kendaraan', 'Mobil', 'Cash', 'Bandung'),
    
    ('2024-04-28', 15, 10000.00, 'Kendaraan', 'Motor', 'Cash', 'Jambi');

Pertama, itu membuat sebuah database bernama "prio2" dan kemudian menggunakan database tersebut.

Selanjutnya, itu membuat sebuah tabel bernama "Penjualan" di dalam database "prio2" dengan kolom-kolom yang sesuai.

Setelah tabel dibuat, itu memasukkan beberapa baris data ke dalam tabel "Penjualan".

Terakhir, itu melakukan query untuk menghitung total penjualan per kategori produk setiap bulan.


Hasil dari query dibawah ini akan memberikan ringkasan total penjualan per kategori produk untuk setiap bulan yang terdapat dalam data penjualan. Setiap baris hasil akan mencakup tahun, bulan, kategori produk, dan total penjualan untuk kombinasi tersebut.

    SELECT EXTRACT(YEAR FROM tanggal_transaksi) AS tahun,

        EXTRACT(MONTH FROM tanggal_transaksi) AS bulan,

        kategori_produk,

        SUM(jumlah_penjualan) AS total_penjualan

    FROM Penjualan

    GROUP BY tahun, bulan, kategori_produk

    ORDER BY tahun, bulan, kategori_produk;

