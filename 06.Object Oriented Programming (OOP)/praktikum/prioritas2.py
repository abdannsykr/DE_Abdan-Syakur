class KelasLatihan:

    def __init__ (self, jenisLatihan, jadwal):
        self.jenisLatihan = jenisLatihan
        self.jadwal = jadwal

    def jenis(self):
       return "\nJenis Latihan      : " + self.jenisLatihan + "\nJadwal Latihan     : " + self.jadwal

class Yoga(KelasLatihan):
    def __init__(self, jenisLatihan, jadwal, tingkatKesulitan):
        super().__init__(jenisLatihan, jadwal)
        self.tingkatKesulitan = tingkatKesulitan

    def aturPosisiYoga(self):
        return "Sirsa padasana"

    def jenis(self):
        return super().jenis() + "\nPosisi Yoga        : " + self.aturPosisiYoga() + "\nTingkat kesulitan  : " + self.tingkatKesulitan

class AngkatBeban(KelasLatihan):
    def __init__(self, AngkatBeban, jadwal, BeratMaksimum):
        super().__init__(AngkatBeban, jadwal)
        self.BeratMaksimum = BeratMaksimum

    def aturBeratBeban(self):
        return "10kg"

    def jenis(self):
        return super().jenis() + "\nBerat beban        : " + self.aturBeratBeban() + "\nBerat Maksimum     : " + self.BeratMaksimum

gaya = Yoga ("Yoga","Senin","Sulit")
angkatbeban = AngkatBeban ("Angkat beban", "Sabtu", str(20)+"kg")
print(gaya.jenis())
print(angkatbeban.jenis())
    
