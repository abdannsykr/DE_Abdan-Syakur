## Rangkuman Relational Database

### Database Relationship
one to one : setiap entitas hanya dapat memiliki relasi dengan satu entitas lain.
one to many : satu entitas dapat memiliki relasi dengan beberapa entitas, begitu pula sebaliknya.
many to many : entitas yang ada dapat memiliki relasi dengan entitas lain, begitu pula sebaliknya.

### DDL
dimanfaatkan guna membuat ataupun memodifikasi struktur pada suatu objek pada database yang paling utama untuk pembuatan skema.

### DML
perintah yang digunakan untuk memanipulasi data dalam tabel dari suatu database.

### DCL
komponen SQL yang berfungsi untuk mengontrol data.

### Join
sebuah klausa untuk mengkombinasikan record dari dua atau lebih tabel.

### Join Standar Sql Ansi
inner join : mengembalikan baris - baris dari dua tabel atau lebih yang memenuhi syarat.
left join : mengembalikan seluruh baris dari tabel disebelah kiri yang dikenai kondisi ON dan hanya baris dari tabel disebelah kanan yang memenuhi kondisi join.
right join : mengembalikan semua baris dari tabel sebelah kanan yang dikenai kondisi ON dengan data dari tabel sebelah kiri yang memenuhi kondisi join.

### Fungsi Agregasi Sql
min : fungsi dimana nilai beberapa baris dikelompokkan bersama untuk membentuk nilai ringkasan tunggal.
max : digunakan untuk mendapatkan nilai maximum atau nilai terbesar dari sebuah data record ditabel.
sum : digunakan untuk mendapatkan jumlah total nilai dari sebuah data atau record di tabel.
avg : digunakan untuk mencari nilai rata - rata dari sebuah data atau record di tabel.
count : digunakan untuk mencari jumlah dari sebuah data atau record di tabel.
having : digunakan untuk menyeleksi data berdasarkan kriteria tertentu, dimana kriteria berupa fungsi aggregat.

### Subquery
subquery atau inner query atau nested query adalah query didalam query sql lain.
sebuah subquery digunakan untuk mengembalikan data yang akan digunakan dalam query utama sebagai syarat untuk lebih membatasi data yang akan diambil.