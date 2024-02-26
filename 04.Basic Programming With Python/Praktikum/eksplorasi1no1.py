def cek_anagram(kata1, kata2):
    # Menghapus spasi dan mengubah huruf menjadi huruf kecil
    kata1 = kata1.replace(" ", "").lower()
    kata2 = kata2.replace(" ", "").lower()

    # Membuat dictionary untuk menghitung frekuensi huruf pada kata pertama
    frekuensi1 = {}
    for huruf in kata1:
        if huruf in frekuensi1:
            frekuensi1[huruf] += 1
        else:
            frekuensi1[huruf] = 1

    # Membuat dictionary untuk menghitung frekuensi huruf pada kata kedua
    frekuensi2 = {}
    for huruf in kata2:
        if huruf in frekuensi2:
            frekuensi2[huruf] += 1
        else:
            frekuensi2[huruf] = 1

    # Memeriksa apakah kedua dictionary frekuensi huruf sama
    return frekuensi1 == frekuensi2

# Input kata pertama dan kata kedua
kata_pertama = input("Kata pertama: ")
kata_kedua = input("Kata kedua: ")

# Memeriksa apakah kata tersebut adalah anagram atau bukan
if cek_anagram(kata_pertama, kata_kedua):
    print("Anagram")
else:
    print("Bukan Anagram")
