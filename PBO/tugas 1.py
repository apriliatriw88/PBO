#class mahasiswa:
#    "dasar kelas untuk semua mahasiswa"
#    jmlMhs = 0
#    def __init__ (self, nama, prodi):
#        self.nama = nama
#        self.prodi = prodi
#        mahasiswa.jmlMhs += 1
#    def tampilJml(self):
#        print("Total Mahasiswa: ", mahasiswa.jmlMhs)
#    def tampilProfil(self):
#        print("Nama : ", self.nama)
#        print("Nama : ", self.prodi)
#        print()
#mhs1 = mahasiswa("Adi","Teknik Informatika")
#mhs2 = mahasiswa("Budi","Matematika")
#mhs1.tampilProfil()
#mhs2.tampilProfil()

#tugas 1
class ayam:
    "dasar kelas untuk ayam"
    jmlAyam = 0
    def __init__ (self, jenis, warna, jenis_kelamin):
        self.jenis = jenis
        self.warna = warna
        self.jenis_kelamin = jenis_kelamin
        ayam.jmlAyam += 1
    def tampilJml(self):
        print("Total Ayam: ", ayam.jmlAyam)
    def tampilProfil(self):
        print("Jenis : ", self.jenis)
        print("Warna : ", self.warna)
        print("Jenis kelamin : ", self.jenis_kelamin)
        print()
ay = ayam("Ayam kampung","Putih", "betina")
aym = ayam("Ayam Cemani", "Hitam pekat", "jantan")
ay.tampilProfil()
aym.tampilProfil()

#tugas 2
aya = ayam('', '', '')

jns = input("jenis : ")
wrn = input("warna : ")
jk = input("jenis kelamin : ")
telur = input("petelur : ")
berkaki = input("kaki : ")

setattr(aya,'jenis',jns)
setattr(aya,'warna',wrn)
setattr(aya,'jenis kelamin',jk)
setattr(aya,'petelur',telur)
setattr(aya,'kaki',berkaki)

print("=====================")
print(getattr(aya,'jenis'))
print(hasattr(aya,'warna'))

print("======================")
print(delattr(aya,berkaki))
aya.tampilProfil()


