class masyarakat :
    def __init__(self, nama, nik, alamat, agama) :
        self.nama = input ("masukan nama : ")
        self.__nik = input ("masukan nik : ")
        setattr(masyarakat,'__nik',self.__nik)
        self.alamat = input ("masukan alamat : ")
        self.agama = input("masukan agama : ")

    def tampil(self):
        print(' Tampil masyarakat')
        print("nama \t: ",self.nama)
        print("nik \t: ",getattr(masyarakat,'__nik'))
        print("alamat \t: ",self.alamat)
        print('agama \t:',self.agama)

class mahasiswa(masyarakat) :       
    def _init_ (self, nama, tg_lahir, prodi, nim, nama_ortu):
        masyarakat._init_(self, nama, nik, alamat, agama)
        self.nama = input ("masukan nama : ")
        self.__lahir = input ("masukan tanggal lahir : ")
        setattr(mahasiswa,'__lahir',self.__lahir)
        self.prodi = input("masukan prodi : ")
        self.nim = input("masukan nim : ")
        self.nama_ortu = input(" masukan nama ortu : ")
    def univ(self):
        print(input("masukan nama universitas : "))
    def data(self):
        masyarakat.tampil(self)
        print('mahasiswa')
        print("nama : ",self.nama)
        print('tgl lahir : ',getattr(mahasiswa,'__lahir'))
        print("prodi \t: ",self.prodi)
        print("nim : ",self.nim)
        print("Nama ortu : ", self.nama_ortu)

class dosen(masyarakat) :
    def _init_ (self, nama, nip, nama_ortu):
        masyarakat._init_(self, nama, nik, alamat, agama)
        self.nama = input("masukan nama : ")
        self.nip = input("masukan nip : ")
        self.nama_ortu = input("masukan nama ortu : ")
    def mengajar(self):
        self.nama_universitas = input ("masukan nama universitas : ")
        self.prodi_ajar = input ("masukan prodi ajar : ")

    def tmp(self): 
        masyarakat.tampil(self)
        print("nama : ",self.nama)
        print("Nama ortu : ",self.nama_ortu)
        print('nip dosen \t: ',self.nip)
        print("Tempat Megajar dosen : ",self.nama_universitas)
        print("Prodi dosen mengajar : ",self.prodi_ajar)

ms1= masyarakat ('','','','')
mhs1= mahasiswa('','','','')
ds1 = dosen('','','','')
ms1.tampil()
print("Data Mahasiswa")
mhs1.univ()
mhs1.data()
print("Data Dosen")
ds1.mengajar()
ds1.tmp()
