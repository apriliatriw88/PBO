# class pintu:
#    def __init__(self):
#       print('============')
#       print('PINTU BIASA')
#       print('============')
#       self.status = "tutup"
#       print('status awal:', self.status)
#    def buka(self):
#       self.status = "buka"
#       print('buka pintu:', self.status)
#    def tutup(self):
#       self.status = "tutup"
#       print('tutup pintu:', self.status)  
#    def is_buka(self):
#       print('apakah pintu terbuka? ', end='')
#       return self.status == "buka"
# class pintuBoolean:
#    def __init__(self):
#       print('=============')
#       print('PINTU BOOLEAN')
#       print('=============')
#       self.status = False
#       print('status awal:', self.status)
#    def buka(self):
#       self.status = True
#       print('buka pintu : ', self.status)
#    def tutup(self):
#       self.status = False
#       print('buka pintu : ', self.status)
#    def is_buka(self):
#       print('apakah pintu terbuka?', end='')
#       return self.status

# a= pintu()
# print(a.buka())
# print(a.tutup())
# print(a.is_buka())

# b=pintuBoolean()
# print(b.buka())
# print(b.tutup())
# print(b.is_buka())



# class hewan:
#    def __init__(self):
#       print('============')
#       print('HEWAN')
#       print('============')
#       self.JenisHewan = "karnivora"
#       setattr(hewan, 'JenisHewan', self.JenisHewan)
#       self.JenisKelamin ='jantan'
#       setattr(hewan, 'JenisKelamin', self.JenisKelamin)
#       self.Habitat = 'hutan'
#       setattr(hewan, 'Habitat', self.Habitat)
#    def suara(self):
#       print('terdengar')
#    def tampilhewan(self):
#       print('jenis hewan : ', getattr(hewan, 'JenisHewan'))
#       print('jenis kelamin : ', getattr(hewan, 'JenisKelamin'))
#       print('habitat : ', getattr(hewan, 'Habitat'))

# class kucing(hewan):
#    def __init__(self):
#       print('=============')
#       print('KUCING')
#       print('=============')
#       self.JenisKucing = 'kucing persia'
#    def suara(self):
#       print('mengeong')
#    def tampilkucing(self):
#       hewan.tampilhewan(self)
#       print('jenis kucing : ', self.JenisKucing)

# class anjing(hewan):
#    def __init__(self):
#       print('=============')
#       print('ANJING')
#       print('=============')
#       self.JenisAnjing = 'Anjing pudel'
#    def suara(self):
#       print('menggonggong')
#    def tampilanjing(self):
#       hewan.tampilhewan(self)
#       print('jenis anjing : ', self.JenisAnjing)

# hw=hewan()
# hw.suara()
# hw.tampilhewan()

# kc=kucing()
# kc.suara()
# kc.tampilkucing()

# an=anjing()
# an.suara()
# an.tampilanjing()


# class buku:
#    def __init__(self):
#       print('\n============')
#       print('BUKU')
#       print('============')
#       self.penulis = input('penulis : ')
#       setattr(buku, 'penulis', self.penulis)
#       self.penerbit = input('penerbit : ')
#       setattr(buku, 'penerbit', self.penerbit)
#       self.TahunTerbit = input('tahun terbit : ')
#       setattr(buku, 'TahunTerbit', self.TahunTerbit)
#    def jenis(self):
#       self.jenis = input('jenis buku : ')
#    def tampil(self):
#       print('penulis : ', getattr(buku, 'penulis'))
#       print('penerbit : ', getattr(buku, 'penerbit'))
#       print('tahun terbit : ', getattr(buku, 'TahunTerbit'))
#       print('jenis buku : ', self.jenis)

# class novel(buku):
#    def __init__(self):
#       print('\n=============')
#       print('NOVEL')
#       print('=============')
#       buku.jenis(self)
#    def jenisnovel(self):
#       self.jenisnovel = input('jenis novel : ')
#    def tampilnovel(self):
#       print('jenis novel : ', self.jenisnovel)

# class pelajaran(buku):
#    def __init__(self):
#       print('\n=============')
#       print('PELAJARAN')
#       print('=============')
#       buku.jenis(self)
#    def jenispelajaran(self):
#       self.jenispelajaran = input('jenis pelajaran : ')
#    def tampilpelajaran(self):
#       print('jenis pelajaran : ', self.jenispelajaran)

# bk = buku()
# bk.jenis()
# bk.tampil()

# nv = novel()
# nv.jenisnovel
# nv.tampilnovel()

# pl = pelajaran()
# pl.jenispelajaran()
# pl.tampilpelajaran()



# class BangunDatar:
#    def __init__(self):
#       self.keliling = input('keliling : ')
#       setattr(BangunDatar, 'keliling', self.keliling)
#       self.luas = input('luas : ')
#       setattr(BangunDatar, 'luas', self.luas)
#    def hitungluas(self):
#       print('hitung luas')
#    def hitungkeliling(self) :
#       print('hitung keliling')
#    def tampil(self):
#       print('luas : ', getattr(BangunDatar, 'luas'))
#       print('keliling : ', getattr(BangunDatar, 'keliling'))

# class lingkaran(BangunDatar):
#    def __init__(self):
#       self.jari = int(input('masukan jari-jari : '))
#       self.phi = int(input('masukan phi : '))
#    def hitungluaslingkaran(self):
#       self.luas = float(self.phi*self.jari*self.jari)
#       print('\nluas lingkaran : ', self.luas)
#    def hitungkelilinglingkaran(self):
#       self.keliling = float(2*self.phi*self.jari)
#       print('\nkeliling lingkaran : ', self.keliling)
#    def tampillingkaran(self):
#       BangunDatar.tampil(self)
      

# class segitiga(BangunDatar):
#    def __init__(self):
#       self.alas = int(input('masukan alas: '))
#       self.tinggi = int(input('masukan tinggi : '))
#    def hitungluassegitiga(self):
#       self.luas = float((self.alas*self.tinggi)/2)
#       print('\nluas segitiga : ', self.luas)
#    def hitungkelilingsegitiga(self):
#       self.sisi = int(input('\nmasukan sisi : '))
#       self.keliling = float(self.sisi+self.sisi+self.sisi)
#       print('keliling segitiga : ', self.keliling)
#    def tampilsegitiga(self):
#       BangunDatar.tampil(self)

# bd=BangunDatar()
# ln=lingkaran()
# sg=segitiga()

# while True :
#    bd.tampil()
#    print('\nSILAHKAN PILIH')
#    print('1. LINGKARAN')
#    print('2. SEGITIGA')
#    print('3. Keluar\n')

#    pilihan = int(input('masukan pilihan : '))
#    if pilihan == 1 :
#       bd.tampillingkaran()
#       print('LINGKARAN')
#       ln.hitungluaslingkaran()
#       ln.hitungkelilinglingkaran()
#    elif pilihan == 2 :
#       sg.tampilsegitiga()
#       print('SEGITIGA')
#       sg.hitungluassegitiga()
#       sg.hitungkelilingsegitiga()
#    else :
#       print('keluar')
#       break




class hewan :
   def __init__(self) :
      print('================')
      print('hewan')
      print('================')
      self.jenishewan = 'karnivora'
      setattr(hewan, 'jenishewan', self.jenishewan)
      self.jeniskelamin = 'jantan'
      setattr(hewan, 'jeniskelamin', self.jeniskelamin)
      self.habitat = 'hutan'
      setattr(hewan, 'habitat', self.habitat)
   def suara (self) :
      print('terdengar...')
   def tampilhewan (self) :
      print('jenis hewan : ', getattr(hewan, 'jenishewan'))
      print('jenis kelamin : ', getattr(hewan, 'jeniskelamin'))
      print('habitat : ', getattr(hewan, 'habitat'))

class kucing (hewan) :
   def __init__(self) :
      print('============')
      print('kucing')
      print('==============')
      self.jeniskucing = 'persia'
   def suara (self) :
      print('mengeong')
   def tampilkucing (self) :
      hewan.tampilhewan(self)
      print('jenis kucing : ', self.jeniskucing)

class anjing (hewan) :
   def __init__(self) :
      print('=============')
      print('anjing')
      print('=============')
      self.jenisanjing = 'buldog'
   def suara (self) :
      print('menggonggong')
   def tampilanjing (self) :
      hewan.tampilhewan(self)
      print('jenis anjing :', self.jenisanjing)

h = hewan()
h.suara()
h.tampilhewan()

k = kucing()
k.suara()
k.tampilkucing()

a = anjing()
a.suara()
a.tampilanjing()