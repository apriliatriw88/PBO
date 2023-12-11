print('_______NAMA KELOMPOK 6_______')
print('1. Aprilia Tri Widiyastuti (212103005)')
print('2. Leli Rahmaningrum (212103008)')
print('3. Rifa Melati N (212103036)')


class ayah :
    def __init__(self) :
        self.skill = ''
        self.warnakulit =''
    def InputDataAyah(self) :
        print('\nMasukan data dengan benar')
        print('\n======DATA AYAH======')
        self.skill = input('masukan skill : ')
        setattr(ayah, 'skill', self.skill)
        self.warnakulit = input('masukan warna kulit : ')
        setattr(ayah, 'warnakulit', self.warnakulit)
    def TampilDataAyah(self) :
        print('Skill : ', getattr(ayah, 'skill'))
        print('warna kulit : ', getattr(ayah, 'warnakulit'))

class ibu :
    def __init__(self) :
        self.sifat = ''
        self.rambut = ''
    def InputDataIbu(self) :
        print('\n======DATA IBU=====')
        self.sifat = input('masukan sifat : ')
        setattr(ibu, 'sifat', self.sifat)
        self.rambut = input('masukan rambut : ')
        setattr(ibu, 'rambut', self.rambut)
    def TampilDataIbu(self) :
        print('sifat : ', getattr(ibu, 'sifat'))
        print('rambut : ', getattr(ibu, 'rambut'))

class anak(ayah, ibu) :
    def __init__(self) :
        self.nama = None
        self.__umur = None
        ayah.__init__(self)
        ibu.__init__(self)
    def InputDataAnak(self) :
        print('\n=====DATA ANAK=====')
        self.nama = input('masukan nama : ')
        self.__umur = input('masukan umur : ')
    def TampilDataAnak(self) :
        ayah.TampilDataAyah(self)
        ibu.TampilDataIbu(self)
        print('nama : ', self.nama)
        print('umur : ', self.__umur)

ank = anak()
ank.InputDataAyah()
ank.InputDataIbu()
ank.InputDataAnak()
ank.TampilDataAnak()






    
