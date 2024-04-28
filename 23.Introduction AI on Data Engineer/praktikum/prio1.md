Input_1 :

 ![alt text](https://github.com/abdannsykr/DE_Abdan-Syakur/blob/main/23.Introduction%20AI%20on%20Data%20Engineer/screenshot/input1.jpg)

Output_1 :

 ![alt text](https://github.com/abdannsykr/DE_Abdan-Syakur/blob/main/23.Introduction%20AI%20on%20Data%20Engineer/screenshot/output1.jpg)

Entitas:

Pelanggan (Customers):

    customer_id (PK)
    
    nama_pelanggan
    
    alamat
    
    nomor_telepon

Produk (Products):
    
    product_id (PK)
    
    nama_produk
    
    harga
    
    stok

Pesanan (Orders):
    
    order_id (PK)
    
    customer_id (FK)
    
    tanggal_pesanan
    
    total_harga

Detail Pesanan (Order_Details):
    
    order_detail_id (PK)
    
    order_id (FK)
    
    product_id (FK)
    
    jumlah
    
    harga_per_barang

Hubungan:

Setiap Pelanggan dapat membuat banyak Pesanan (One-to-Many: Pelanggan ke Pesanan)
Setiap Pesanan dapat memiliki banyak Detail Pesanan (One-to-Many: Pesanan ke Detail Pesanan)
Setiap Produk dapat memiliki banyak Detail Pesanan (One-to-Many: Produk ke Detail Pesanan)
Dalam skema ini, setiap pesanan memiliki satu pelanggan yang membuatnya dan berisi detail pesanan yang mencakup produk apa yang dibeli dan berapa banyak. Produk memiliki detail pesanan yang terkait untuk melacak penjualan dan stok.

Input_2 :

 ![alt text](https://github.com/abdannsykr/DE_Abdan-Syakur/blob/main/23.Introduction%20AI%20on%20Data%20Engineer/screenshot/input2.jpg)

Output_2 :

 ![alt text](https://github.com/abdannsykr/DE_Abdan-Syakur/blob/main/23.Introduction%20AI%20on%20Data%20Engineer/screenshot/output2.jpg)

CREATE TABLE Customers (
    
    customer_id INT PRIMARY KEY,
    
    nama_pelanggan VARCHAR(100),
    
    alamat VARCHAR(255),
    
    nomor_telepon VARCHAR(20)

    );

CREATE TABLE Products (

    product_id INT PRIMARY KEY,

    nama_produk VARCHAR(100),

    harga DECIMAL(10, 2),

    stok INT

    );

CREATE TABLE Orders (

    order_id INT PRIMARY KEY,

    customer_id INT,

    tanggal_pesanan DATE,

    total_harga DECIMAL(10, 2),

    FOREIGN KEY (customer_id) REFERENCES Customers(customer_id)

    );

CREATE TABLE Order_Details (

    order_detail_id INT PRIMARY KEY,

    order_id INT,

    product_id INT,

    jumlah INT,

    harga_per_barang DECIMAL(10, 2),

    FOREIGN KEY (order_id) REFERENCES Orders(order_id),

    FOREIGN KEY (product_id) REFERENCES Products(product_id)

    );

Input_3 :

 ![alt text](https://github.com/abdannsykr/DE_Abdan-Syakur/blob/main/23.Introduction%20AI%20on%20Data%20Engineer/screenshot/input3.jpg)

Output_3 :

 ![alt text](https://github.com/abdannsykr/DE_Abdan-Syakur/blob/main/23.Introduction%20AI%20on%20Data%20Engineer/screenshot/output3.jpg)

Menampilkan semua pelanggan:

    SELECT * FROM Customers;

Menampilkan semua produk:

    SELECT * FROM Products;

Menampilkan semua pesanan beserta nama pelanggan:

    SELECT Orders.order_id, Customers.nama_pelanggan, Orders.tanggal_pesanan, Orders.total_harga

    FROM Orders

    JOIN Customers ON Orders.customer_id = Customers.customer_id;

Menampilkan semua detail pesanan serta nama produk:

    SELECT Order_Details.order_detail_id, Products.nama_produk, Order_Details.jumlah, Order_Details.harga_per_barang

    FROM Order_Details

    JOIN Products ON Order_Details.product_id = Products.product_id;

Menampilkan semua pesanan berserta detailnya (termasuk nama produk dan jumlah):

    SELECT Orders.order_id, Products.nama_produk, Order_Details.jumlah, Order_Details.harga_per_barang

    FROM Orders

    JOIN Order_Details ON Orders.order_id = Order_Details.order_id

    JOIN Products ON Order_Details.product_id = Products.product_id;

Menampilkan total harga pesanan untuk setiap pesananan:

    SELECT order_id, SUM(jumlah * harga_per_barang) AS total_harga

    FROM Order_Details

    GROUP BY order_id;

Input_4 :

 ![alt text](https://github.com/abdannsykr/DE_Abdan-Syakur/blob/main/23.Introduction%20AI%20on%20Data%20Engineer/screenshot/input4.jpg)

Output_4 :

 ![alt text](https://github.com/abdannsykr/DE_Abdan-Syakur/blob/main/23.Introduction%20AI%20on%20Data%20Engineer/screenshot/output4.jpg)


Pada skema database pembelian produk elektronik yang telah dibuat sebelumnya, terjadi beberapa hubungan antar entitas yang menciptakan struktur database yang disebut sebagai relational database. Berikut adalah penjelasan tentang relational database dalam konteks pembelian produk elektronik:

Pelanggan (Customers) dan Pesanan (Orders):
 
Hubungan antara pelanggan dan pesanan bersifat One-to-Many, yang berarti satu pelanggan dapat melakukan banyak pesanan, tetapi setiap pesanan hanya dimiliki oleh satu pelanggan.
Setiap pesanan (order) terkait dengan satu pelanggan melalui kolom customer_id pada tabel Orders.

Pesanan (Orders) dan Detail Pesanan (Order_Details):

Hubungan antara pesanan dan detail pesanan juga bersifat One-to-Many, yang berarti satu pesanan dapat memiliki banyak detail pesanan, tetapi setiap detail pesanan hanya terkait dengan satu pesanan.
Setiap detail pesanan (order detail) terkait dengan satu pesanan melalui kolom order_id pada tabel Order_Details.

Produk (Products) dan Detail Pesanan (Order_Details):

Hubungan antara produk dan detail pesanan juga bersifat One-to-Many, yang berarti satu produk dapat terdapat dalam banyak detail pesanan, tetapi setiap detail pesanan hanya terkait dengan satu produk.
Setiap detail pesanan (order detail) terkait dengan satu produk melalui kolom product_id pada tabel Order_Details.

Dengan struktur hubungan yang tepat ini, database dapat mengorganisir data dengan baik dan memungkinkan untuk melacak informasi seperti produk yang dibeli oleh pelanggan tertentu, pesanan apa yang dilakukan oleh pelanggan, dan detail pesanan termasuk produk apa yang dibeli dan jumlahnya. Ini memfasilitasi operasi bisnis seperti manajemen stok, pelacakan penjualan, dan analisis pelanggan.

Penjelasan Hasil:

- Buat penjelasan singkat mengenai bagaimana AI memproses input dan menghasilkan output.

   
   Dalam konteks pembelian produk elektronik, proses AI dimulai dengan input data yang mencakup informasi pelanggan seperti nama, alamat, dan nomor telepon, informasi produk seperti nama, harga, dan stok, serta informasi pesanan seperti tanggal pesanan dan jumlah barang yang dipesan. Sebelum data digunakan oleh model AI, proses preprocessing mungkin diperlukan untuk memurnikan atau memproses data lebih lanjut, seperti normalisasi data pelanggan dan produk ke dalam format yang konsisten, atau penghapusan noise atau outlier. Model AI yang diterapkan dalam skenario ini bisa berupa model klasifikasi untuk memprediksi apakah suatu pesanan adalah penipuan berdasarkan pola pembelian yang mencurigakan, atau model rekomendasi untuk menghasilkan rekomendasi produk yang disesuaikan dengan preferensi pelanggan berdasarkan sejarah pembelian mereka. Model AI akan memproses data yang dimasukkan untuk mencari pola atau fitur yang relevan, seperti pola pembelian yang tidak biasa atau preferensi pelanggan. Output yang dihasilkan oleh model AI bisa berupa prediksi apakah suatu pesanan adalah penipuan atau bukan, rekomendasi produk untuk pelanggan tertentu, atau informasi lainnya seperti perkiraan waktu pengiriman atau rencana stok barang. Output kemudian dievaluasi untuk memastikan keakuratannya, dan jika diperlukan, data atau model dapat diperbarui untuk meningkatkan kinerjanya. Dengan menerapkan proses AI dalam skenario pembelian produk elektronik, perusahaan dapat meningkatkan efisiensi operasional, meningkatkan pengalaman pelanggan, dan mengurangi risiko seperti penipuan atau kekurangan stok.

- Jelaskan potensi aplikasi hasil ini dalam konteks Data Engineering.

   
   Dalam konteks Data Engineering, hasil dari proses AI dalam skenario pembelian produk elektronik dapat dioptimalkan untuk berbagai aplikasi yang memberikan nilai tambah bagi perusahaan. Insinyur data dapat merancang dan mengimplementasikan pipeline data yang mengambil data dari berbagai sumber seperti database transaksional, sistem pelacakan interaksi pelanggan, dan data eksternal lainnya. Data ini kemudian diolah dan dimuat ke dalam sistem analisis untuk memahami perilaku pelanggan, preferensi pembelian, dan tren pasar, yang kemudian dapat digunakan untuk meningkatkan strategi pemasaran dan penjualan. Dalam situasi di mana keputusan harus diambil dengan cepat, seperti mendeteksi penipuan transaksi atau memberikan rekomendasi produk saat pelanggan sedang berbelanja online, insinyur data dapat membangun infrastruktur yang memungkinkan pemrosesan data secara real-time. Teknologi seperti Apache Kafka atau Apache Flink dapat digunakan untuk memproses data secara cepat dan efisien, memungkinkan perusahaan untuk merespons dengan cepat terhadap perubahan pasar atau perilaku pelanggan. Insinyur data juga bertanggung jawab untuk merancang dan mengelola data warehouse atau data lake yang menyimpan semua data terkait pembelian produk elektronik dengan aman dan terstruktur. Data ini dapat diakses dengan mudah untuk analisis lebih lanjut, dan skema yang sesuai serta performa yang optimal akan memastikan data dapat digunakan secara efektif untuk pengambilan keputusan. Dengan memanfaatkan teknik-teknik seperti collaborative filtering, content-based filtering, atau model deep learning, insinyur data dapat mengoptimalkan sistem rekomendasi untuk meningkatkan pengalaman pelanggan dan meningkatkan penjualan dengan memberikan rekomendasi produk yang relevan. Terakhir, dengan membangun sistem monitoring yang memantau kinerja sistem secara real-time, mendeteksi anomali, dan memberikan wawasan yang dibutuhkan untuk meningkatkan kualitas dan efisiensi proses, perusahaan dapat terus mengoptimalkan operasinya. Dengan menerapkan praktik Data Engineering yang cermat, hasil dari proses AI dalam skenario pembelian produk elektronik dapat dimanfaatkan secara efektif untuk mengoptimalkan operasi bisnis, meningkatkan pengalaman pelanggan, dan menghasilkan wawasan yang bernilai bagi perusahaan.


