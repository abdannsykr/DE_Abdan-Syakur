## Rangkuman Data Transformation

### Introduction to Data Transformation
Data Transformation mengacu pada proses pengonversian data dari satu format atau struktur ke format atau struktur lainnya. Ini adalah langkah fundamental dalam proses integrasi data. 

### Normalization Scaling data to a standard range.
tujuan: Memastikan bahwa setiap fitur memberikan kontribusi yang sama terhadap komputasi dalam algoritma pembelajaran mesin.
metode umum: penskalaan min-maks, normalisasi skor-z.
kasus penggunaan: jaringan saraf, algoritma yang mengandalkan besaran fitur.

### Encoding Converting categorical data numerical format.
tujuan: algoritma pembelajaran mesin memerlukan masukan numerik, sehingga data kategorikal harus dikonversi.
metode umum:
    - pengkodean one-hot: menetapkan kolom biner untuk setiap kategori.
    - pengkodean label: menetapkan bilangan bulat unik untuk setiap kategori.
kasus penggunaan: analisis regresi, tugas klasifikasi.

