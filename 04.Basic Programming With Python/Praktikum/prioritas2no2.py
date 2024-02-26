def hitung_skor_budget(budget):
    if budget >= 0 and budget <= 50:
        return 4
    elif budget >= 51 and budget <= 80:
        return 3
    elif budget >= 81 and budget <= 100:
        return 2
    else:
        return 1

def hitung_skor_waktu(waktu):
    if waktu >= 0 and waktu <= 20:
        return 10
    elif waktu >= 21 and waktu <= 30:
        return 5
    elif waktu >= 31 and waktu <= 50:
        return 2
    else:
        return 1

def hitung_skor_kesulitan(kesulitan):
    if kesulitan >= 0 and kesulitan <= 3:
        return 10
    elif kesulitan >= 4 and kesulitan <= 6:
        return 5
    elif kesulitan >= 7 and kesulitan <= 10:
        return 1
    else:
        return 0

# Input budget, waktu pengerjaan, dan tingkat kesulitan
budget = float(input("Budget: "))
waktu = int(input("Waktu pengerjaan: "))
kesulitan = int(input("Tingkat kesulitan: "))

# Menghitung skor dari setiap faktor
skor_budget = hitung_skor_budget(budget)
skor_waktu = hitung_skor_waktu(waktu)
skor_kesulitan = hitung_skor_kesulitan(kesulitan)

# Menghitung total skor
total_skor = skor_budget + skor_waktu + skor_kesulitan

# Menentukan hasil prioritas proyek
if total_skor >= 24 and total_skor <= 17:
    hasil = "High"
elif total_skor >= 16 and total_skor <= 10:
    hasil = "Medium"
elif total_skor >= 9 and total_skor <= 3:
    hasil = "Low"
else:
    hasil = "Impossible"

# Menampilkan output
print("Output:", hasil)
