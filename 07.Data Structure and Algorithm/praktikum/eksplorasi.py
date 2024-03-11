import uuid

pengeluaran = {}

def tambah_pengeluaran(Name, jumlah):
    id_pengeluaran = str(uuid.uuid4())
    pengeluaran[id_pengeluaran] = {'Name': Name, 'jumlah': jumlah}
    print(f"Data pengeluaran untuk {Name} dengan ID {id_pengeluaran} telah ditambahkan.")

def lihat_pengeluaran():
    total_pengeluaran = sum(p['jumlah'] for p in pengeluaran.values())
    print("Daftar Pengeluaran:")
    for id_pengeluaran, data in pengeluaran.items():
        print(f"ID: {id_pengeluaran}\nName: {data['Name']}\nJumlah: {data['jumlah']}")
    print(f"Total Pengeluaran: {total_pengeluaran}")

def ubah_pengeluaran(id_pengeluaran, Name, jumlah):
    if id_pengeluaran in pengeluaran:
        pengeluaran[id_pengeluaran] = {'Name': Name, 'jumlah': jumlah}
        print(f"Data pengeluaran dengan ID {id_pengeluaran} telah diubah.")
    else:
        print(f"Data pengeluaran dengan ID {id_pengeluaran} tidak ditemukan.")

def hapus_pengeluaran(id_pengeluaran):
    if id_pengeluaran in pengeluaran:
        del pengeluaran[id_pengeluaran]
        print(f"Data pengeluaran dengan ID {id_pengeluaran} telah dihapus.")
    else:
        print(f"Data pengeluaran dengan ID {id_pengeluaran} tidak ditemukan.")

while True:
    print("===========Menu===========")
    print("1. Tambah Data Pengeluaran")
    print("2. Lihat Data Pengeluaran")
    print("3. Ubah Data Pengeluaran")
    print("4. Hapus Data Pengeluaran")
    print("5. Keluar")
    print("==========================")

    pilihan = input("Masukkan pilihan : ")

    if pilihan == '1':
        Name = input("Masukkan nama pengeluaran: ")
        jumlah = int(input("Masukkan jumlah pengeluaran: "))
        tambah_pengeluaran(Name, jumlah)
    elif pilihan == '2':
        lihat_pengeluaran()
    elif pilihan == '3':
        id_pengeluaran = input("Masukkan ID pengeluaran yang ingin diubah: ")
        Name = input("Masukkan nama pengeluaran yang baru: ")
        jumlah = int(input("Masukkan jumlah baru: "))
        ubah_pengeluaran(id_pengeluaran, Name, jumlah)
    elif pilihan == '4':
        id_pengeluaran = input("Masukkan ID pengeluaran yang ingin dihapus: ")
        hapus_pengeluaran(id_pengeluaran)
    elif pilihan == '5':
        print("Terima kasih!")
        break
    else:
        print("Pilihan tidak valid. Silakan masukkan pilihan yang sesuai.")
