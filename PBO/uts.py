class lingkaran :
    def __init__(self) :
        self.phi = ''
        self.jari_jari = ''
    def luas (self) :
        self.phi = 3.14
        self.jari_jari = 10
        self.luas = float(self.phi*self.jari_jari*self.jari_jari)
        print('\nluas lingkaran : ', self.luas)
    def tampil(self) :
        print('\nLUAS LINGKARAN')

ln = lingkaran()
ln.tampil()
ln.luas()


class lingkaran :
    def __init__(self) :
        self.phi = ''
        self.jari_jari = ''
        self.__diameter = ''
    def luas (self) :
        self.phi = int(input('\nmasukan phi : '))
        self.jari_jari = int(input('masukan jari jari : '))
        self.luas = float(self.phi*self.jari_jari*self.jari_jari)
        print('\nluas lingkaran : ', self.luas)
    def keliling (self) :
        self.phi = int(input('\nmasukan phi : '))
        self.__diameter = int(input('masukan diameter : '))
        self.keliling = float(self.phi*self.__diameter)
        print('\nkeliling lingkaran : ', self.keliling)
    def tampil(self):
        print('\nLINGKARAN')

ln = lingkaran()
ln.tampil()
ln.luas()
ln.keliling()





class pemilik :
    def __init__(self) :
        self.id = ''
        self.nama =''
        self.JumlahInvestasi = ''
    def InputDataPemilik(self) :
        print('\nMasukan data dengan benar')
        print('\n======DATA PEMILIK SAHAM======')
        self.id = input('masukan id : ')
        setattr(pemilik, 'id', self.id)
        self.nama = input('masukan nama : ')
        setattr(pemilik, 'nama', self.nama)
        self.JumlahInvestasi = input('masukan jumlah investasi : ')
        setattr(pemilik, 'JumlahInvestasi', self.JumlahInvestasi)
    def TampilDataPemilik(self) :
        print('id : ', getattr(pemilik, 'id'))
        print('nama : ', getattr(pemilik, 'nama'))
        print('jumlah investasi : ', getattr(pemilik, 'JumlahInvestasi'))

class pemain :
    def __init__(self) :
        self.idpemain = ''
        self.nama_pemain = ''
    def InputDataPemain(self) :
        print('\n======DATA PEMAIN=====')
        self.idpemain = input('masukan id pemain : ')
        setattr(pemain, 'idpemain', self.idpemain)
        self.nama_pemain = input('masukan nama pemain : ')
        setattr(pemain, 'nama_pemain', self.nama_pemain)
    def TampilDataPemain(self) :
        print('id pemain : ', getattr(pemain, 'idpemain'))
        print('nama pemain : ', getattr(pemain, 'nama_pemain'))

class club (pemilik,pemain) :
    def __init__(self) :
        self.idclub = None
        self.namaclub = None
        self.namapelatih = None
        pemilik.__init__(self)
        pemain.__init__(self)
    def InputDataClub(self) :
        print()
        self.idclub = input('masukan id club : ')
        self.namaclub = input('masukan nama club : ')
        self.namapelatih = input('masukan nama pelatih : ')
    def TampilDataClub(self) :
        print('\nDATA CLUB')
        pemilik.TampilDataPemilik(self)
        pemain.TampilDataPemain(self)
        print('id club : ', self.idclub)
        print('nama club : ', self.namaclub)
        print('nama pelatih : ', self.namapelatih)

cl = club()
cl.InputDataPemilik()
cl.InputDataPemain()
cl.InputDataClub()
cl.TampilDataClub()