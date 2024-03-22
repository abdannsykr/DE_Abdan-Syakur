## Rangkuman Docker

### What is Virtual Machine?
- Sebuah representasi virtual dari sebuah komputer.
- Berbagai program dapat dijalankan didalam Virtual Machine (VM).

### What is Container?
Sebuah unit yang "membungkus" kode beserta dependensinya (library) sehingga aplikasi dapat dijalankan dengan cepat dan andal (reliable) di berbagai environment.

### Container VS Virtual Machine
Container :
    - Abstraksi di layer aplikasi
    - Menggunakan kapasitas yang lebih kecil (biasanya dalam puluhan MB)
    - Booting lebih cepat karena biasanya hanya berisi satu aplikasi saja
    - Digunakan untuk membungkus sebuah aplikasi. Satu container untuk satu aplikasi

Virtual Machines :
    - Abstraksi di hardware fisik
    - Setiap VM berisi satu sistem operasi secara penuh sehingga menggunakan kapasitas yang lebih banyak
    - Booting lebih lambat
    - Digunakan untuk menjalankan komputer dalam bentuk virtual

### What is Docker?
Docker adalah sebuah container manager yang dapat digunakan untuk mengelola aplikasi dalam bentuk container.

### Dockerfile Cheat Sheet
FROM : Mendapatkan image dari docker registry
RUN : Menjalankan command ketika membuat container
ENV : Menentukan environment variable didalam container
ADD : Menyalin file dengan process yang lain
COPY : Menyalin copy file kedalam container
WORKDIR : Menentukan working directory
ENTRYPOINT : Menjalankan command ketika container sudah dibuat
CMD : Menjalankan command tapi bisa diganti / overwrite

### Docker Basic Commands
docker container create : Membuat container baru
    contoh : docker container create -it --name redis1 redis:latest
docker container start : Menjalankan container
    contoh : docker container start redis1
docker container stop : Menghentikan container
    contoh : docker container stop redis1
docker container rm : Menghapus container. Container harus dalam kondisi mati
    contoh : docker container rm redis1
docker container rm -f : Menghapus container meskipun container masih running
    contoh : docker container rm -f redis2
docker container ls docker ps : Melihat semua container yang sedang running
docker container ls -a docker ps -a : Melihat semua container (running maupun mati)
docker images : Melihat semua docker image yang tersedia di lokal / host
docker pull : Mengunduh docker image
    contoh : docker pull redis:latest
docker push : Mempublish docker image ke docker hub
    contoh : docker push myimage:1.0.0
docker run : Membuat dan menjalankan container
    contoh : docker run -itd --name redis-app redis:latest
docker exec : Menjalankan command didalam container
    contoh : docker exec -it redis-app redis-cli
docker logs : Melihat log dari container 
    contoh : docker logs redis-app
docker inspect : Melihat informasi secara rinci mengenai container
    contoh : docker inspect redis-app
docker volume create : Mmebuat docker volume baru
    contoh : docker volume create myvolume
docker volume ls : Menampilkan semua docker volume
    contoh : -
docker volume prune : Menghapus docker volume yang tidak terpakai
    contoh : -
docker network create : Membuat docker network baru
    contoh : docker network create mynetwork
docker network connect : Menyambungkan docker network kepada container yang sedang running maupun yang mati
    contoh : docker network connect mynetwork myapi

### What is Docker Volume?
Sebuah mekanisme penyimpanan data yang dapat digunakan agar data tetap ada (persistent).

### Why Docker Volume?
Backup dan migrasi lebih mudah, Dapat dibagi lebih aman dengan container lain, Menambahkan fungsionalitas lain.

### What is Docker Network?
Sebuah jaringan yang dapat digunakan antar container untuk berkomunikasi satu sama lain.

### What is Container Orchestration?
- Sebuah mekanisme untuk mengelola berbagai container.
- Container orchestration cocok digunakan untuk mengelola sistem yang dibangun dengan berbagai container seperti microservices.

### What is Docker Compose?
- Sebuah container orchestration yang sudah disediakan oleh Docker.
- Docker compose dapat digunakan untuk menjalankan berbagai container dengan membuat file konfigurasi dalam format YAML.