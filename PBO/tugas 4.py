class masyarakat :
    def __init__(self) :
        self.nama=""
        self.__nik=""
    def inputDataMasyarakat(self):
        print('masukan data sesuai perintah')
        self.nama = input('masukan nama : ')
        setattr(masyarakat, 'nama', self.nama)
        self.__nik=input('masukan nik : ')
        setattr(masyarakat, '__nik', self.__nik)
    def tampilDataMasyarakat(self):
        print('nama : ', getattr(masyarakat, 'nama'))
        print("nik : ", getattr(masyarakat, '__nik'))

class mahasiswa(masyarakat) :
    def __init__(self) :
        self.NPM = None
        self.univ = None
        masyarakat.__init__(self)
    def inputDataMahasiswa(self) :
        print()
        self.NPM =input('masukan nomor pokok mhs : ')    
        self.univ = input ('masukan universitas : ')
    def tampilDataMahasiswa(self):
        masyarakat.tampilDataMasyarakat(self)
        print('nomor pokok mhs : ',self.NPM)
        print('universitas : ', self.univ)

class dosen(masyarakat) :
    def __init__(self) :
        self.__NIDN = None
        self.kampus = None
        self.prodi = None
        masyarakat.__init__(self)
    def inputDataDosen(self) :
        print()
        self.__NIDN = input('masukan nomor induk dosen nasional : ')
        self.kampus = input('masukan tempat ngajar : ')
        self.prodi = input('masukan studi yang diajar : ')
    def tampilDataDosen(self) :
        masyarakat.tampilDataMasyarakat(self)
        print('nomor induk dosen nasional : ', self.__NIDN)
        print('tempat mengajar : ',self.kampus)
        print('studi yang diajar : ', self.prodi)

mhs = mahasiswa()
dsn = dosen()

while True :
    mhs.inputDataMasyarakat()
    print('pilihan : ')
    print('1. Mahasiswa')
    print('2. Dosen')
    print('3. Keluar')

    pilihan = int(input('masukan pilihan : '))

    if pilihan == 1 :
        mhs.inputDataMahasiswa()
        print('\nData Mahasiswa')
        mhs.tampilDataMahasiswa()
    elif pilihan == 2 :
        dsn.inputDataDosen()
        print('\nData Dosen')
        dsn.tampilDataDosen()
    else:
        print('SELESAI')
        break
