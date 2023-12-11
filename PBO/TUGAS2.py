class mahasiswa:
    def _init_ (self, nama, prodi, nim):
        self.nama = nama
        self.prodi = prodi
        self.nim = nim

    def tampilProfil(self):
        print("Nama : ", self.nama)
        print("Prodi : ", self.prodi)
        print("NIM : ", self.nim)
        print()

mhs1 = mahasiswa('','','')
name = input("Nama : ")
sp = input("Prodi : ")
sn = input("NIM : ")

setattr(mhs1, "nama", name)
setattr(mhs1, "prodi", sp)
setattr(mhs1, "nim", sn)

mhs1.tampilProfil()

class mahasiswa:
    def _init_ (self, nama, prodi, nim, kelamin, fakultas):
        self.nama = nama
        self.prodi = prodi
        self.nim = nim
        self.kelamin = kelamin
        self.fakultas = fakultas

    def tampilProfil(self):
        print("Nama : ", self.nama)
        print("Prodi : ", self.prodi)
        print("Nim : ", self.nim)
        print("Jenis kelamin : ", self.kelamin)
        print("Fakultas : ", self.fakultas)
        print()

mhs1 = mahasiswa(" "," ", " "," ", " ")
name = input("nama : ")
sp = input("prodi : ")
sn = input("nim : ")
sk = input("jenis kelamin : ")
sf = input("fakultas : ")

setattr(mhs1, "nama", name)
setattr(mhs1, "prodi", sp)
setattr(mhs1, "nim", sn)
setattr(mhs1, "kelamin", sk)
setattr(mhs1, "fakultas", sf)

delattr(mhs1, "kelamin")

mhs1.tampilProfil()

class mahasiswa:
    def _init_ (self, nama, prodi, nim, kelamin, fakultas):
        self.nama = nama
        self.prodi = prodi
        self.nim = nim
        self.kelamin = kelamin
        self.fakultas = fakultas

    def tampilProfil(self):
        print("Nama : ", self.nama)
        print("Prodi : ", self.prodi)
        print("NIM : ", self.nim)
        print("Jenis kelamin : ", self.kelamin)
        print("Fakultas : ", self.fakultas)
        print()

mhs1 = mahasiswa(" "," ", " "," ", " ")
name = input("nama : ")
sp = input("prodi : ")
sn = input("nim : ")
sk = input("jenis kelamin : ")
sf = input("fakultas : ")

setattr(mhs1, "nama", name)
setattr(mhs1, "prodi", sp)
setattr(mhs1, "nim", sn)
setattr(mhs1, "kelamin", sk)
setattr(mhs1, "fakultas", sf)

print(getattr("Jenis Kelamin : ", mhs1, "kelamin"))