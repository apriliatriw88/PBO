# class pegawai :
#     def __init__(self) :
#         self.nip = ''
#         self.nama = ''
#         self.jabatan = ''
#         self.gajipokok = ''
#         self.tunjangan = ''
#         self.pajak = ''
#     def inputdatapegawai(self) :
#         print('\nMASUKAN DATA DENGAN BENAR')
#         self.nip = input('masukan nip : ')
#         setattr(pegawai, 'nip', self.nip)
#         self.nama = input('masukan nama : ')
#         setattr(pegawai, 'nama', self.nama)
#         self.jabatan = input('masukan jabatan : ')
#         setattr(pegawai, 'jabatan', self.jabatan)
#         self.gajipokok = input('masukan gaji pokok : ')
#         setattr(pegawai, 'gajipokok', self.gajipokok)
#         self.tunjangan = input('masukan tunjangan : ')
#         setattr(pegawai, 'tunjangan', self.tunjangan)
#         self.pajak = input('masukan pajak : ')
#         setattr(pegawai, 'pajak', self.pajak)
#     def tampildatapegawai(self) :
#         print('nip : ', getattr(pegawai, 'nip'))
#         print('nama : ', getattr(pegawai, 'nama'))
#         print('jabatan : ', getattr(pegawai, 'jabatan'))
#         print('gaji pokok : ', getattr(pegawai, 'gajipokok'))
#         print('tunjangan : ', getattr(pegawai, 'tunjangan'))
#         print('pajak : ', getattr(pegawai, 'pajak'))

# class sekretaris(pegawai) :
#     def __init__(self):
#         self.upahlembur = None
#         pegawai.__init__(self)
#     def inputsekretaris(self) :
#         print()
#         self.upahlembur = input('masukan upah lembur : ')
#     def tampilsekretaris(self) :
#         pegawai.tampildatapegawai(self)
#         print('upah lembur : ', self.upahlembur)

# class manajer(pegawai) :
#     def __init__(self):
#         self.bonusgaji = None
#         pegawai.__init__(self)
#     def inputmanajer(self) :
#         print()
#         self.bonusgaji = input('masukan bonus : ')
#     def tampilmanajer(self) :
#         pegawai.tampildatapegawai(self)
#         print('bonus : ', self.bonusgaji)

# sk = sekretaris()
# mn = manajer()

# while True :
#     sk.inputdatapegawai()
#     print('\nSILAHKAN PILIH')
#     print('1. Sekretaris')
#     print('2. Manajer')
#     print('3. Keluar')

#     pilihan = int(input('masukan pilihan : '))

#     if pilihan == 1 : 
#         sk.inputsekretaris()
#         print('\n====DATA SEKRETARIS====')
#         sk.tampilsekretaris()
#     elif pilihan == 2 :
#         mn.inputmanajer()
#         print('\n====DATA MANAGER====')
#         mn.tampilmanajer()
#     else :
#         print('\n====SELESAI====')
#         break

class Hero(object):
    def __init__(self, nama=None, iden=None, masuk=None, gapok=None):
        self.nama = nama
        self.iden = iden
        self.masuk = masuk
        self.gapok = gapok

try:
    gaji_harian = 50000
    listPgw = []
    loop = int(input("jumlah data pegawai yang akan dihitung\t:"))
    print() 
    for i in range(loop):
        nama=input("masukan nama pegawai\t:")
        idn=input("masukan nomor id\t:")
        msk=int(input("jumlah hari masuk\t:"))
        gp = msk*gaji_harian
        listPgw.append(Hero(nama,idn,msk,gp))
        print()
        print("-------------------------------------------")
except ValueError:
    print(""" 'jumlah hari masuk' dan 'data pegawai' yang dimasukkan harus angka! """)

print("Gaji Pegawai:\n")
for Hero in listPgw:
    print("Nama\t\t:",Hero.nama)
    print("Nomor identitas\t:",Hero.iden)
    print("hari masuk\t:",Hero.masuk)
    print("gapok\t\t: Rp",Hero.gapok)
    print()
    print("===========================================")

def potongan(cuti):
    assert(cuti.masuk <= 25)
    return print("Presensi <= 25 hari. Gaji dipotong 2.5 %\nTidak mendapat gaji penuh!")

try:
    potongan(listPgw[0])
except AssertionError:
    print("Semua pegawai mendapat gaji penuh!")