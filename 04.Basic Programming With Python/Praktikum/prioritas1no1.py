panjang = float(input("Masukkan panjang persegi panjang: "))
lebar = float(input("Masukkan lebar persegi panjang: "))

# Menghitung luas persegi panjang
luas = panjang * lebar

# Menampilkan luas
print("Luas persegi panjang:", luas)

# Memeriksa apakah luas genap atau ganjil
if luas % 2 == 0:
    print("even rectangle")
else:
    print("odd rectangle")
