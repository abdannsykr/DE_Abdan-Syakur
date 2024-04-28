CREATE DATABASE prio2;

USE prio2;

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

INSERT INTO Penjualan (tanggal_transaksi, jumlah_penjualan, harga, kategori_produk, nama_produk, metode_pembayaran, lokasi_penjualan)
VALUES 
('2024-04-28', 10, 350000.00, 'Elektronik', 'Smartphone', 'Kartu Kredit', 'Jakarta'),
('2024-04-28', 10, 50000.00, 'Kendaraan', 'Mobil', 'Cash', 'Bandung'),
('2024-04-28', 15, 10000.00, 'Kendaraan', 'Motor', 'Cash', 'Jambi');

SELECT EXTRACT(YEAR FROM tanggal_transaksi) AS tahun,
       EXTRACT(MONTH FROM tanggal_transaksi) AS bulan,
       kategori_produk,
       SUM(jumlah_penjualan) AS total_penjualan
FROM Penjualan
GROUP BY tahun, bulan, kategori_produk
ORDER BY tahun, bulan, kategori_produk;
