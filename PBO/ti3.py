#contoh class dan objek
#class jilbab : 
#    def __init__(self):
#        self.model = ''
#        self.merk = ''
#        self.bahan = ''
#    def inputjilbab(self) :
#        self.model = input('masukan model : ')
#        self.merk = input('masukan merk : ')
#        self.bahan = input('masukan bahan : ')
#    def tampiljilbab(self) :
#        print('\nJILBAB')
#        print('model\t : ', self.model)
#        print('merk\t : ', self.merk)
#        print('bahan\t : ', self.bahan)
#jl = jilbab()
#jl.inputjilbab()
#jl.tampiljilbab()

#contoh manipulasi atribut
#class sepatu :
#    def __init__(self, merk, harga, model) :
#        self.merk = merk
#        self.harga = harga
#        self.model = model
#    def tampilProfil(self):
#        print('\nSEPATU')
#        self.merk = input("merk : ")
#        setattr(sepatu, 'merk', self.merk)
#        getattr(sepatu, 'merk')
#        print(hasattr(sepatu, 'merk'))

#        self.harga = input ("harga : ")
#        setattr(sepatu, 'harga', self.harga)
#        getattr(sepatu, 'harga')
#        
#        self.model = input("model : ")
#        setattr(sepatu, 'model', self.model)
#        getattr(sepatu, 'model')

#spt = sepatu('', '', '')
#spt.tampilProfil()

#contoh enkapsulasi
#class pelajar :
#    def __init__(self) :
#        self.nama = ''
#        self.kelas = ''
#        self.__nisn = ''
#    def InputDataAnak(self) :
#        self.nama = input('masukan nama : ')
#        self.kelas = input('masukan kelas : ')
#        self.__nisn = input('masukan nisn : ')
#    def TampilDataAnak(self) :
#        print('\nDATA PELAJAR')
#        print('nama : ', self.nama)
#        print('kelas : ', self.kelas)
#        print('umur : ', self.__nisn)

#plj = pelajar()
#plj.InputDataAnak()
#plj.TampilDataAnak()

#multiple inheritance
class ortu :
    def __init__(self) :
        self.sikap = ''
        self.agama =''
    def InputDataOrtu(self) :
        print('\nMasukan data dengan benar')
        print('\n======DATA ORTU======')
        self.sikap = input('masukan sikap : ')
        setattr(ortu, 'sikap', self.sikap)
        self.agama = input('masukan agama : ')
        setattr(ortu, 'agama', self.agama)
    def TampilDataOrtu(self) :
        print('sikap : ', getattr(ortu, 'sikap'))
        print('agama : ', getattr(ortu, 'agama'))

class guru :
    def __init__(self) :
        self.ilmu = ''
    def InputDataGuru(self) :
        print('\n======DATA GURU=====')
        self.ilmu = input('masukan ilmu : ')
        setattr(guru, 'ilmu', self.ilmu)
    def TampilDataGuru(self) :
        print('ilmu : ', getattr(guru, 'ilmu'))

class murid(ortu, guru) :
    def __init__(self) :
        self.nama = None
        self.__umur = None
        self.kelas = None
        ortu.__init__(self)
        guru.__init__(self)
    def InputDataAnak(self) :
        print()
        self.nama = input('masukan nama : ')
        self.__umur = input('masukan umur : ')
        self.kelas = input('masukan kelas : ')
    def TampilDataAnak(self) :
        print('\nDATA MURID')
        ortu.TampilDataOrtu(self)
        guru.TampilDataGuru(self)
        print('nama : ', self.nama)
        print('umur : ', self.__umur)
        print('kelas : ', self.kelas)

mr = murid()
mr.InputDataOrtu()
mr.InputDataGuru()
mr.InputDataAnak()
mr.TampilDataAnak()






    