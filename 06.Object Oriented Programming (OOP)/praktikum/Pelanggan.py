class pelanggan  :

    def __init__ (self, nama, usia, idPelanggan):
        self.__nama = nama
        self.__usia = usia
        self.__idPelanggan = idPelanggan 

    def getNama(self, nama):
        self.__nama = nama
    
    def setNama(self):
        return self.__nama

    def getUsia(self, usia):
        self.__getUsia = usia
    
    def setUsia(self):
        return self.__setUsia

    def getIdPelanggan(self, idPelanggan):
        self.__getIdPelanggan = idPelanggan

    def setIdPelanggan(self):
        return self.__IdPelanggan
    
    def tampilkanInfo(self):
        print("DATA PELANGGAN")
        print("Nama             : ",self.__nama)
        print("Usia             : ",self.__usia)
        print("IdPelanggan      : ",self.__idPelanggan)
        print()

class pelatih :

    def __init__(self, nama, spesialisasi, tahunPengalaman):
        self.__nama = nama
        self.__spesialisasi = spesialisasi
        self.__tahunPengalaman = tahunPengalaman

    def getNama(self, nama):
        self.__nama = nama

    def setNama(self):
        return self.__nama
    
    def getSpesialisasi(self, spesialisasi):
        self.__spesialisasi = spesialisasi
    
    def setSpesialisasi(self):
        return self.__spesialisasi
    
    def getTahunPengalaman(self, tahunPengalaman):
        self.__tahunPengalaman = tahunPengalaman
    
    def setTahunPengalaman(self):
        return self.__tahunPengalaman
    
    def tampilkanInfo(self):
        print("PELATIH")
        print("Nama              : ", self.__nama)
        print("Spesialis         : ", self.__spesialisasi)
        print("Pengalaman        : ", self.__tahunPengalaman)
        print()

class KelasLatihan(pelatih):

    def __init__ (self, nama, spesialisasi, tahunPengalaman, latihan, jadwal):
        super().__init__(nama, spesialisasi, tahunPengalaman)
        self._nama = nama
        self._latihan = latihan
        self._jadwal = jadwal

    def getlatihan(self):
        return self._latihan

    def setlatihan(self, latihan):
        self._latihan = latihan
        
    def getjadwal(self):
        return self._jadwal
    
    def setjadwal(self, jadwal):
        self._jadwal = jadwal

    def tampilkanInfo(self):
        super().tampilkanInfo()
        print("LATIHAN")
        print("Jenis Latihan     : ", self._latihan)
        print("Jadwal Latihan    : ", self._jadwal)


pelanggan1 = pelanggan ("Abdan", 21, "ABD41")
pelanggan1.tampilkanInfo()


latihan1 = KelasLatihan("Abdan","Futsal", str(3) + "tahun", "Latihan Fisik", "Sabtu")
latihan1.tampilkanInfo()

