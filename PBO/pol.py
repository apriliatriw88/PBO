class buku:
   def __init__(self):
      print('\n============')
      print('BUKU')
      print('============')
      self.penulis = input('penulis : ')
      setattr(buku, 'penulis', self.penulis)
      self.penerbit = input('penerbit : ')
      setattr(buku, 'penerbit', self.penerbit)
      self.TahunTerbit = input('tahun terbit : ')
      setattr(buku, 'TahunTerbit', self.TahunTerbit)
   def jenis(self):
      self.jenis = input('jenis buku : ')
   def tampil(self):
      print('\nBUKUU')
      print('penulis : ', getattr(buku, 'penulis'))
      print('penerbit : ', getattr(buku, 'penerbit'))
      print('tahun terbit : ', getattr(buku, 'TahunTerbit'))
      
class novel(buku):
   def __init__(self):
      buku.jenis(self)
   def jenisnovel(self):
      self.jenisnovel = input('jenis novel : ')
      setattr(novel, 'jenisnovel', self.jenisnovel)
   def tampilnovel(self):
      print('jenis novel : ', getattr(novel, 'jenisnovel'))

class pelajaran(buku):
   def __init__(self):
      buku.jenis(self)
   def jenispelajaran(self):
      self.jenispelajaran = input('jenis pelajaran : ')
   def tampilpelajaran(self):
      print('jenis pelajaran : ', self.jenispelajaran)

bk = buku()
bk.jenis()
bk.tampil()

nv=novel()
pl=pelajaran()

while True :
   print('\nSILAHKAN PILIH')
   print('1. NOVEL')
   print('2. PELAJARAN')
   print('3. Keluar\n')
   pilihan = int(input('masukan pilihan : '))
   if pilihan == 1 :
      nv.jenisnovel
      print('\n=============')
      print('NOVEL')
      print('=============')
      nv.tampilnovel()
   elif pilihan == 2 :
      pl.jenispelajaran()
      print('\n=============')
      print('PELAJARAN')
      print('=============')
      pl.tampilpelajaran()
   else :
      print('keluar')
      break