def hitung_tarif_berat(berat):
    if berat >= 1 and berat <= 20:
        return 10000
    elif berat >= 21 and berat <= 30:
        return 15000
    elif berat >= 31 and berat <= 60:
        return 20000
    else:
        return 45000

def hitung_tarif_jarak(jarak):
    if jarak >= 1 and jarak <= 5:
        return 2000
    elif jarak >= 6 and jarak <= 15:
        return 5000
    elif jarak >= 16 and jarak <= 30:
        return 10000
    else:
        return 15000

# Input berat dan jarak
berat = int(input("Berat: "))
jarak = int(input("Jarak: "))

# Menghitung tarif berdasarkan berat dan jarak
tarif_berat = hitung_tarif_berat(berat)
tarif_jarak = hitung_tarif_jarak(jarak)
tarif_total = tarif_berat + tarif_jarak

# Menampilkan output
print("Output:", tarif_total)
