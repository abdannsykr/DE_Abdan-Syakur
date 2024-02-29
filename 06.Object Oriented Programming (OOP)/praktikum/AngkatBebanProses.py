class KelasLatihan:

    def __init__ (self, jenisLatihan, jadwal):
        self.jenisLatihan = jenisLatihan
        self.jadwal = jadwal

    def tampilkanInfo(self):
        print("Jenis latihan     : ", self.jenisLatihan)
        print("Jadwal latihan    : ", self.jadwal)

class yoga(KelasLatihan):

    def __init__ (self, jenisLatihan, jadwal, tingkatKesulitan):
        super().__init__(jenisLatihan, jadwal)
        self.tingkatKesulitan = tingkatKesulitan

    def aturPosisiYoga (self):
        return "bersila"
    
    def tampilkanInfo(self):
        super().tampilkanInfo()
        print("Tingkat Kesulitan   : ", self.tingkatKesulitan)
        print()

    def tampilkanInfo(self):
        print("Jenis latihan       :  yoga ")
        print("Jadwal latihan      : ", self.jadwal)
        print("Tingkat Kesulitan   : ", self.tingkatKesulitan)
        print("Posisi yoga         : ", self.aturPosisiYoga())
        print()

    
class AngkatBeban(KelasLatihan):

    def __init__(self, jenisLatihan, jadwal, BeratMaksimum):
        super().__init__(jenisLatihan, jadwal)
        self.BeratMaksimum = BeratMaksimum

    def aturBeratBeban(self):
        return "10"
    
    def tampilkanInfo(self):
        super().tampilkanInfo()
        print("Angkat Beban        : ", self.BeratMaksimum)
        

    def tampilkanInfo(self):
        print("Jenis latihan       :  Angkat Beban")
        print("Jadwal latihan      : ", self.jadwal)
        print("Berat Maksimum      : ", self.BeratMaksimum)
        print("Memakai berat beban : ",self.aturBeratBeban())

        

array = [
    yoga("Yoga", "Senin", "Sulit"),
    AngkatBeban("AngkatBeban", "Sabtu", 20,)
]

for latihan in array :
    latihan.tampilkanInfo()
    print()

    
