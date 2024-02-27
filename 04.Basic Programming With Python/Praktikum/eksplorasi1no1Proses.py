def cek_anagram(kata1, kata2):
    kata1 = kata1.replace(" ", "").lower()
    kata2 = kata2.replace(" ", "").lower()

    frekuensi1 = {}
    for huruf in kata1:
        if huruf in frekuensi1:
            frekuensi1[huruf] += 1
        else:
            frekuensi1[huruf] = 1

    frekuensi2 = {}
    for huruf in kata2:
        if huruf in frekuensi2:
            frekuensi2[huruf] += 1
        else:
            frekuensi2[huruf] = 1

    return frekuensi1 == frekuensi2

kata_pertama = input("Kata pertama: ")
kata_kedua = input("Kata kedua: ")

if cek_anagram(kata_pertama, kata_kedua):
    hasil = ("Anagram")
else:
    hasil = ("Bukan Anagram")

print(f"Hasilnya adalah {hasil} ")
