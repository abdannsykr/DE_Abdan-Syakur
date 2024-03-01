class KelasLatihan:

    def __init__ (self, jenisLatihan, jadwal):
        self.jenisLatihan = jenisLatihan
        self.jadwal = jadwal

    def tampilkanInfo(self):
        print("Jenis latihan     : ", self.jenisLatihan)
        print("Jadwal latihan    : ", self.jadwal)

class Yoga(KelasLatihan):
    def __init__(self, jadwal, tingkatKesulitan):
        super().__init__("yoga", jadwal)
        self.tingkatKesulitan = tingkatKesulitan

    def aturPosisiYoga(self):
        self.aturPosisiYoga

    def tampilkanInfo(self):
        print("Jenis latihan      : ", self.jenisLatihan)
        print("Jadwal latihan     : ", self.jadwal)
        print("Tingkat Kesulitan  : ", self.tingkatKesulitan)
        print()

class AngkatBeban(KelasLatihan):
    def __init__(self, jadwal, BeratMaksimum):
        super().__init__("angkat beban", jadwal)
        self.BeratMaksimum = BeratMaksimum

    def aturBeratBeban(self):
        self.aturBeratBeban

    def tampilkanInfo(self):
        print("Jenis latihan      : ", self.jenisLatihan)
        print("Jadwal latihan     : ", self.jadwal)
        print("Berat Maksimum     : ", self.BeratMaksimum)
        print()

latihan = [
    Yoga("senin", "sulit"),
    AngkatBeban("selasa", 5)
]

for latihan_objek in latihan:
    latihan_objek.tampilkanInfo()

    
