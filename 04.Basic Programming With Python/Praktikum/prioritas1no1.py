panjang = int(input("masukan panjang persegi panjang : "))
lebar = int(input("masukan lebar persegi panjang : "))

luas = panjang * lebar

if luas % 2 == 0 :
    status = ("even rectangle")
else:
    status = ("ood rectangle")

print(f"luas persegi panjang adalah : {luas}cm ({status})")
