# from abc import ABC, abstractmethod

# class hewan(ABC) :
#     @abstractmethod
#     def lingkungan(self) :
#         pass

# class ikan(hewan) :
#     def lingkungan(self) :
#         print('air')

# class ayam(hewan) :
#     def lingkungan(self) :
#         print('darat')

# i = ikan()
# i.lingkungan()

# a = ayam()
# a.lingkungan()



# class jilbab :
#     def merk(self):
#         print('merek...')

# class jilbab_instan(jilbab) :
#     def merk(self) :
#         print('RABBANI')

# class jilbab_segitiga(jilbab) :
#     def merk(self) :
#         print('bella square')

# j = jilbab()
# ji = jilbab_instan()
# js = jilbab_segitiga()

# j.merk()
# ji.merk()
# js.merk()



class mahasiswa :
    def __init__(self, nama=None, nim=None, nilai=None) :
        self.nama = nama
        self.nim = nim
        self.nilai = nilai

listmhs = []
for i in range (5) :
    nama = input('\nmasukan nama : ')
    nim = input('masukan nim : ')
    try :
        nilai = int(input('masukan nilai : '))
    except :
        print('Mohon untuk Nilai harus berupa angka')
        break    
    listmhs.append(mahasiswa(nama, nim, nilai))
    
print('\nmahasiswa')
for mahasiswa in listmhs :
    print("\nNama: {}\nNim: {}\nNilai: {}".format(mahasiswa.nama, mahasiswa.nim, mahasiswa.nilai))

# class Mahasiswa(object):
#  """_init_() functions as the class constructor"""
#  def _init_(self, nama=None, matkul=None, nilai=None):
#     self.nama = nama
#     self.matkul = matkul
#     self.nilai = nilai
 
# listMahasiswa = []
# for i in range (5) :
#     try : 
#         nama = input('\nmasukan nama : ')
#         matkul = input('masukan matkul : ')
#         nilai = int(input('masukan nilai : '))
#         listMahasiswa.append(Mahasiswa(nama, matkul, nilai))
#     except :
#         print('Mohon untuk Nilai harus berupa angka')


# print("Daftar Mahasiswa :\n")
# for Mahasiswa in listMahasiswa:
#     print("Nama: {}\nMatkul: {}\nNilai: {}\n\n".format(Mahasiswa.nama, Mahasiswa.matkul, 
# Mahasiswa.nilai))