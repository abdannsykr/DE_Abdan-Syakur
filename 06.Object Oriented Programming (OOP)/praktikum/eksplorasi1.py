class KelasLatihan:

    def __init__ (self, jenisLatihan, jadwal):
        self.jenisLatihan = jenisLatihan
        self.jadwal = jadwal
        self.kelas = "tersedia"

    def jenis(self):
       return "\nJenis Latihan      : " + self.jenisLatihan + "\nJadwal Latihan     : " + self.jadwal
    
    def pesanKelas(self):
        if self.kelas == "tersedia":
            self.kelas = "dipesan"
            return "Kelas berhasil di pesan"
        else:
            return "Kelas tidak tersedia"
        
    def batalkanKelas(self):
        if self.kelas == "dipesan":
            self.kelas = "tersedia"
            return "Kelas dibatalkan"
        else:
            return "Kelas tidak bisa dibatalkan"

class Yoga(KelasLatihan):
    def __init__(self, jenisLatihan, jadwal, tingkatKesulitan):
        super().__init__(jenisLatihan, jadwal)
        self.tingkatKesulitan = tingkatKesulitan

    def aturPosisiYoga(self):
        return "Sirsa padasana"

    def jenis(self):
        return super().jenis() + "\nPosisi Yoga        : " + self.aturPosisiYoga() + "\nTingkat kesulitan  : " + self.tingkatKesulitan
    
    def pesanKelas(self):
        if self.kelas == "tersedia":
            self.kelas = "dipesan"
            return "Kelas yoga berhasil di pesan"
        else:
            return "Kelas yoga tidak tersedia"
        
    def batalkanKelas(self):
        if self.kelas == "dipesan":
            self.kelas = "tersedia"
            return "Kelas yoga dibatalkan"
        else:
            return "Kelas yoga tidak bisa dibatalkan"

class AngkatBeban(KelasLatihan):
    def __init__(self, AngkatBeban, jadwal, BeratMaksimum):
        super().__init__(AngkatBeban, jadwal)
        self.BeratMaksimum = BeratMaksimum

    def aturBeratBeban(self):
        return "10kg"

    def jenis(self):
        return super().jenis() + "\nBerat beban        : " + self.aturBeratBeban() + "\nBerat Maksimum     : " + self.BeratMaksimum
    
    def pesanKelas(self):
        if self.kelas == "tersedia":
            self.kelas = "dipesan"
            return "Kelas angkat beban berhasil di pesan"
        else:
            return "Kelas angkat beban tidak tersedia"
        
    def batalkanKelas(self):
        if self.kelas == "dipesan":
            self.kelas = "tersedia"
            return "Kelas angkat beban dibatalkan"
        else:
            return "Kelas angkat beban tidak bisa dibatalkan"

gaya = Yoga ("Yoga","Senin","Sulit")
angkatbeban = AngkatBeban ("Angkat beban", "Sabtu", str(20)+"kg")

print("Pesan kelas Yoga:")
print(gaya.pesanKelas())

print("\nBatalkan kelas Yoga:")
print(gaya.batalkanKelas())

print("\nPesan kelas AngkatBeban:")
print(angkatbeban.pesanKelas())

print("\nBatalkan kelas AngkatBeban:")
print(angkatbeban.batalkanKelas())
