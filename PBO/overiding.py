class atletolahraga:
  def olahraga(self):
    print('olahraga..')

class volly(atletolahraga):
  def olahraga(self):
    print('passing atas')

class sepakbola(atletolahraga):
    def olahraga(self):
        print('meenendang bola')

class lari(atletolahraga):
    def olahraga(self):
        print('lari maraton')

atlet = atletolahraga()
vol = volly()
sep = sepakbola()
lr = lari()

atlet.olahraga()
vol.olahraga()
sep.olahraga()
lr.olahraga()



#class Kendaraan:
#  def berjalan(self):
#    print('berjalan..')

#class Mobil(Kendaraan):
#  def berjalan(self, kecepatan, satuan = 'km/j'):
#    print(f'Berjalan dengan kecepatan {kecepatan} {satuan}')

#sepeda = Kendaraan()
#sedan = Mobil()

#sepeda.berjalan()
#sedan.berjalan(150)



#class KelasTurunan(KelasInduk):
#  def __init__(self):
#    super().__init__()
#class Kendaraan:
#  def berjalan(self):
#    print('berjalan..')

#class Mobil(Kendaraan):
#  def berjalan(self, kecepatan, satuan = 'km/j'):
#    super().berjalan()
#    print(f'  -> dengan kecepatan {kecepatan} {satuan}')

#sepeda = Kendaraan()
#sedan = Mobil()

#sepeda.berjalan()
#sedan.berjalan(150)   