# 1. Sebuah rumah sakit bernama Alta Medika ingin mengelola berbagai data yang telah dikumpulkan seperti data pasien, data komplain, data survei kepuasan pelayanan, data dokter dan data lainnya. Untuk mengelola berbagai data tersebut dapat dilakukan dengan mengembangkan sebuah data pipeline. Berdasarkan kasus ini sebutkan jenis data pipeline yang cocok digunakan beserta alasannya!

Batch Data Pipeline:
Alasan: Batch data pipeline cocok untuk mengelola data yang tidak memerlukan pemrosesan real-time. Data seperti data pasien, data dokter, dan data komplain dapat diambil dan diproses secara batch pada interval waktu tertentu, misalnya harian atau mingguan. Batch processing memungkinkan untuk melakukan analisis yang lebih kompleks dan menyeluruh terhadap data yang dikumpulkan.
Sumber: Marz, N., & Warren, J. (2015). Big Data: Principles and best practices of scalable real-time data systems. Manning Publications Co.

Real-Time Data Pipeline:
Alasan: Untuk data survei kepuasan pelayanan dan data yang membutuhkan respons cepat, seperti data sensor monitor pasien, real-time data pipeline adalah pilihan yang tepat. Dengan menggunakan teknologi seperti Apache Kafka atau Apache Flink, rumah sakit dapat memproses data secara langsung saat datang dan mengambil tindakan yang sesuai dengan cepat.
Sumber: Shukla, A. (2020). Stream Processing with Apache Flink: Fundamentals, Implementation, and Operation of Streaming Applications. O'Reilly Media, Inc.

Hybrid Data Pipeline:
Alasan: Karena rumah sakit Alta Medika memiliki berbagai jenis data dengan karakteristik yang berbeda, penggunaan hybrid data pipeline bisa menjadi solusi yang baik. Hybrid data pipeline menggabungkan keunggulan batch dan real-time processing, sehingga memungkinkan pengolahan data yang efisien dan responsif terhadap kebutuhan bisnis.

Sumber referensi :

     O'Leary, C. (2018). Modern Big Data Processing with Hadoop: Expert techniques for architecting end-to-end Big Data solutions to get valuable insights. Packt Publishing Ltd.