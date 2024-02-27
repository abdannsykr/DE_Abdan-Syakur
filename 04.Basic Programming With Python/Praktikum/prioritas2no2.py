def hitung_budget(budget):
    if budget <= 50:
        return 4
    elif budget <= 80:
        return 3
    elif budget <= 100:
        return 2
    else:
        return 1

def hitung_waktu_pengerjaan(waktu_pengerjaan):
    if waktu_pengerjaan <= 20:
        return 10
    elif waktu_pengerjaan <= 30:
        return 5
    elif waktu_pengerjaan <= 50:
        return 2
    else:
        return 1

def hitung_tingkat_kesulitan(tingkat_kesulitan):
    if tingkat_kesulitan <= 3:
        return 10
    elif tingkat_kesulitan <= 6:
        return 5
    elif tingkat_kesulitan <= 10:
        return 1
    else:
        return 0

def hitung_skor_total(budget, waktu_pengerjaan, tingkat_kesulitan):
    skor_budget = hitung_budget(budget)
    skor_waktu_pengerjaan = hitung_waktu_pengerjaan(waktu_pengerjaan)
    skor_tingkat_kesulitan = hitung_tingkat_kesulitan(tingkat_kesulitan)
    return skor_budget + skor_waktu_pengerjaan + skor_tingkat_kesulitan

def menentukan_prioritas(skor_total):
    if skor_total >= 17 and skor_total <= 24:
        return "High"
    elif skor_total >= 10 and skor_total <= 16:
        return "Medium"
    elif skor_total >= 3 and skor_total <= 9:
        return "Low"
    else:
        return "Impossible"

nama_proyek = input("Masukkan nama proyek: ")
budget = int(input("Masukkan budget: "))
waktu_pengerjaan = int(input("Masukkan waktu pengerjaan: "))
tingkat_kesulitan = int(input("Masukkan tingkat kesulitan: "))

skor_total = hitung_skor_total(budget, waktu_pengerjaan, tingkat_kesulitan)

prioritas = menentukan_prioritas(skor_total)

print(f"Hasil prioritas proyek {nama_proyek} adalah {prioritas}")
