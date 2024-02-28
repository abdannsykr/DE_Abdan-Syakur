class pelanggan  :

    def __init__ (self, nama, usia, idPelanggan):
        self._nama = nama
        self._usia = usia
        self._idPelanggan = idPelanggan 

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
        print("Data Pelanggan")
        print("nama         : ",self._nama)
        print("usia         : ",self._usia)
        print("idPelanggan  : ",self._idPelanggan)
    
    
pelanggan1 = pelanggan ("abdan", 21, "ABD41")
pelanggan1.tampilkanInfo()