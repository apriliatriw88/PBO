#class MakhlukHidup :
#    def __init__(self) :
#        self.tempat_tinggal=""
#    def inputDataMakhlukHidup(self):
#        print('\n==MASUKAN DATA DENGAN BENAR==')
#        self.tempat = input('masukan tempat tinggal : ')
#        setattr(MakhlukHidup, 'tempat tinggal', self.tempat)
#    def tampilDataMakhlukHidup(self):
#        print('tempat tinggal : ', getattr(MakhlukHidup, 'tempat tinggal'))

#class masyarakat(MakhlukHidup) :
#    def __init__(self) :
#        self.nama=None
#        self.__nik=None
#        MakhlukHidup.__init__(self)
#    def inputDataMasyarakat(self):
#        print()
#        self.nama = input('masukan nama : ')
#        self.__nik=input('masukan nik : ')
#    def tampilDataMasyarakat(self):
#        MakhlukHidup.tampilDataMakhlukHidup(self)
#        print('nama : ', self.nama)
#        print("nik : ", self.__nik)

#class mahasiswa(MakhlukHidup) :
#    def __init__(self) :
#        self.NPM = None
#        self.univ = None
#        MakhlukHidup.__init__(self)
#    def inputDataMahasiswa(self) :
#        print()
#        self.NPM =input('masukan nomor pokok mhs : ')    
#        self.univ = input ('masukan universitas : ')
#    def tampilDataMahasiswa(self):
#        MakhlukHidup.tampilDataMakhlukHidup(self)
#        print('nomor pokok mhs : ',self.NPM)
#        print('universitas : ', self.univ)

#class dosen(MakhlukHidup) :
#    def __init__(self) :
#        self.__NIDN = None
#        self.kampus = None
#        self.prodi = None
#        MakhlukHidup.__init__(self)
#    def inputDataDosen(self) :
#        print()
#        self.__NIDN = input('masukan nomor induk dosen nasional : ')
#        self.kampus = input('masukan tempat ngajar : ')
#        self.prodi = input('masukan studi yang diajar : ')
#    def tampilDataDosen(self) :
#        MakhlukHidup.tampilDataMakhlukHidup(self)
#        print('nomor induk dosen nasional : ', self.__NIDN)
#        print('tempat mengajar : ',self.kampus)
#        print('studi yang diajar : ', self.prodi)

#msy = masyarakat()
#mhs = mahasiswa()
#dsn = dosen()

#while True :
#    mhs.inputDataMakhlukHidup()
#    print('pilihan : ')
#    print('1. Masyarakat')
#    print('2. Mahasiswa')
#    print('3. Dosen')
#    print('4. Keluar')

#    pilihan = int(input('masukan pilihan : '))

#    if pilihan == 1 :
#        msy.inputDataMasyarakat()
#        print('\n====Data Masyarakat====')
#        msy.tampilDataMasyarakat()
#    elif pilihan == 2 :
#        mhs.inputDataMahasiswa()
#        print('\n====Data Mahasiswa====')
#        mhs.tampilDataMahasiswa()
#    elif pilihan == 3 :
#        dsn.inputDataDosen()
#        print('\n====Data Dosen====')
#        dsn.tampilDataDosen()
#    else:
#        print('===SELESAI===')
#        break

class makhlukhidup :
    def __init__(self):
        self.TempatTinggal=''
    def inputDataMakhlukHidup(self):
        print('\nMASUKAN DATA YANG SESUAI\n')
        self.TempatTinggal = input ('masukan tempat tinggal : ')
        setattr(makhlukhidup, 'TempatTinggal', self.TempatTinggal)
    def tampilDataMakhlukHidup(self) :
        print('Tempat Tinggal\t\t\t\t:', getattr(makhlukhidup, 'TempatTinggal'))

class masyarakat(makhlukhidup) :
    def __init__(self):
        self.nama = ''
        self.__nik = ''
        makhlukhidup.__init__(self)
    def inputDataMasyarakat(self):
        print()
        self.nama = input('masukan nama\t\t\t\t:')
        setattr(masyarakat, 'nama', self.nama)
        self.__nik = input('masukan nik\t\t\t\t:')
        setattr(masyarakat, '__nik', self.__nik)
    def tampilDataMasyarakat(self) :
        makhlukhidup.tampilDataMakhlukHidup(self)
        print('nama\t\t\t\t\t:',getattr(masyarakat, 'nama'))
        print('nik\t\t\t\t\t\t:', getattr(masyarakat, '__nik'))

class mahasiswa(masyarakat) :
    def __init__(self):
        self.npm = None
        self.univ = None
        masyarakat.__init__(self)
    def inputDataMahasiswa(self):
        print()
        self.npm = input('masukan nomor pokok mahasiswa\t\t:')
        self.univ = input('masukan universitas\t\t\t:')
    def tampilDataMahasiswa(self) :
        masyarakat.tampilDataMasyarakat(self)
        print('nomor pokok mahasiswa\t\t\t:',self.npm)
        print('universitas\t\t\t\t:',self.univ)

class dosen(masyarakat) :
    def __init__(self) :
        self.__nidn = ''
        self.kampus = ''
        self.prodi = ''
        masyarakat.__init__(self)
    def inputDataDosen(self) :
        print()
        self.__nidn = input('masukan nomor pokok dosen nasional : ')
        setattr(dosen, '__nidn', self.__nidn)
        self.kampus = input('masukan tempat mengajar\t\t:')
        setattr(dosen, 'kampus', self.kampus)
        self.prodi = input('masukan program studi\t\t : ')
        setattr(dosen, 'prodi', self.prodi)
    def tampilDataDosen(self) :
        masyarakat.tampilDataMasyarakat(self)
        print('nomor induk dosen nasional\t\t:', getattr(dosen, '__nidn'))
        print('tempat mengajar \t\t\t:', getattr(dosen, 'kampus'))
        print('program studi yang diajar\t\t:', getattr(dosen, 'prodi'))

class dosenTetap(dosen):
    def __init__(self):
        self.__nip = None
        dosen.__init__(self)
    def inputDataDosenTetap(self):
        print()
        self.__nip = input('masukan nomor induk pegawai : ')
    def tampilDataDosenTetap(self) :
        dosen.tampilDataDosen(self)
        print('nomor induk pegawai\t\t\t:', self.__nip)

class dosenTidakTetap(dosen):
    def __init__(self):
        self.tahunAjaran = None
        dosen.__init__(self)
    def inputDataDosenTidakTetap(self):
        print()
        self.tahunAjaran = input('masukan tahun ajaran\t\t\t:')
    def tampilDataDosenTidakTetap(self):
        dosen.tampilDataDosen(self)
        print('tahun ajaran\t\t\t\t:', self.tahunAjaran)

mhs = mahasiswa()
dsn = dosen()
dsnTetap = dosenTetap()
dsnTidakTetap = dosenTidakTetap()

while True :
    mhs.inputDataMakhlukHidup()
    mhs.inputDataMasyarakat()
    print('\nSILAHKAN PILIH')
    print('1. Data Mahasiswa')
    print('2. Data Dosen')
    print('3. Keluar\n')

    pilihan = int(input('masukan pilihan : '))

    if pilihan == 1 :
        mhs.inputDataMahasiswa()
        print()
        print("DATA MAHASISWA")
        mhs.tampilDataMahasiswa()

        kemana = input('kembali mengulang isi data? (y/t) : ')
        if kemana == 'y' :
            print()
        else:
            print('TERIMA KASIH')
            break

    elif pilihan == 2 :
        dsn.inputDataDosen()
        print()
        print('DATA DOSEN UMUM')
        dsn.tampilDataDosen()

        print('\nSILAHKAN MASUKAN PILIHAN')
        print('1. DATA DOSEN TETAP')
        print('2. DATA DOSEM TIDAK TETAP')
        print('3. KELUAR')

        pilihan = int(input('masukan pilihan : '))

        if pilihan == 1 :
            dsnTetap.inputDataDosenTetap()
            print('DATA DOSEN TETAP')
            dsnTetap.tampilDataDosenTetap()
        elif pilihan == 2 :
            dsnTidakTetap.inputDataDosenTidakTetap()
            print()
            print('DATA DOSEN TIDAK TETAP')
            dsnTidakTetap.tampilDataDosenTidakTetap()
        else :
            print('TERIMA KASIH')
            break

        kemana = input('kembali mengulang isi data? (y/t) : ')
        if kemana == 'y' :
            print()
        else:
            print('TERIMA KASIH')
            break
    else : 
        print('TERIMA KASIH')
        break