# print('LIST')
# list1 = ['UNJANI', 'sistem informasi', 2019, 2018]
# list2 = [4, 1, 2, 5, 3]
# list3 = ["a", "b", "c", "d"]
# print("List 1: ",list1)
# print("List 2: ",list2)
# print("List 3: ",list3)

# # perintah mengurutkan list 2
# list2.sort()

# # perintah menambahkan elemen list 3
# list3.append("e")

# # menghapus elemen dari list 1
# list1.remove(2019)

# print("\nPanjang List 1: ", len(list1))
# print("Nilai terbesar pada List 2: ", max(list2))
# print("Mengurutkan List 2: ", list2)
# print("Menambahkan elemen pada List 3: ", list3)
# print("Menghapus elemen pada List 1: ", list1)



# print('\nDICT')
# d_nilai = {'andi':'A','budi':'B','citra':'C','hendra':'A','baron':'D'}
# print("daftar nilai: ",d_nilai)

# # mengecek panjang dictionary
# print("panjang dictionary: ",len(d_nilai),"\n")

# # merubah entry yang sudah ada
# d_nilai['citra']='B'
# print("perubahan 1: ",d_nilai)

# # menambah entry baru
# d_nilai['tony']='A'
# print("perubahan 2: ",d_nilai)

# # mengecek panjang dictionary
# print("panjang dictionary: ",len(d_nilai),"\n")

# # menghapus entry
# del d_nilai['citra']
# print("perubahan 3: ",d_nilai)
# print("panjang dictionary: ",len(d_nilai),"\n")

# # mengosongkan dictionary
# d_nilai.clear()
# print("perubahan 4: ",d_nilai)
# print("panjang dictionary: ",len(d_nilai),"\n")


# print('SET')
# # set data campuran 
# data = {1, 2.0, "jarvis", (3,4,5)} 
# print('Set gabungan: ',data) 

# # bila kita mengisi duplikasi, set akan menghilangkan salah satu
# # output: {1,2,3} 
# angka = {1,2,2,3,3,3} 
# print('Set angka:',angka) 

# # set tidak bisa berisi anggota list 
# # contoh berikut akan muncul error TypeError 
# # set_baru = {1,2,[3,4,5]} 
# # supaya bisa program bisa jalan, baris diatas dikomen atau dihapus

# # menambah anggota baru pada set angka
# angka.add(4) 
# print('Set angka perubahan 1:',angka)

# # menambah beberapa anggota sekaligus
# angka.update([3,4,5,6]) 
# print('Set angka perubahan 2:',angka)

# # mengosongkan set
# angka.clear()
# print('Set angka perubahan 3:',angka)

# # Membuat set A and B 
# A = {1, 2, 3, 4, 5} 
# B = {4, 5, 6, 7, 8} 
# print('A:',A)
# print('B:',B)

# # Gabungan menggunakan operator | 
# print('A gabung B: ',(A | B))

# # Irisan menggunakan operator & 
# print('A irisan B: ',(A & B))

# # operasi selisih
# print('A - B: ',(A - B))
# # operasi komplemen

# print('A komplemen B: ',(A ^ B))


# #penggunaan colection pada pbo
# class Hero(object):
#  """__init__() functions as the class constructor"""
#  def __init__(self, nama=None, alias=None, kelompok=None):
#     self.nama = nama
#     self.alias = alias
#     self.kelompok = kelompok
 
# listHero = []
# listHero.append(Hero("Anthony Edward Stark","Iron Man","Avengers"))
# listHero.append(Hero("Peter Jason Quill","Star-Lord","Guardians of Galaxy"))
# listHero.append(Hero("Barry Allen","The Flash","Justice League"))
# listHero.append(Hero("Thor Odinson","God of Thunder","Avengers"))
# listHero.append(Hero("Bruce Wayne","Batman","Justice League"))

# print ("Hero pertama:", listHero[0].nama,"\n")
# print("Daftar superhero:\n")
# for Hero in listHero:
#     print("Nama: {}\nAlias: {}\nKelompok: {}\n\n".format(Hero.nama, Hero.alias, Hero.kelompok))


# #latihan 1

# class Hero(object):
#  """__init__() functions as the class constructor"""
#  def __init__(self, nama=None, alias=None, kelompok=None, list_hero=None):
#     self.nama = nama
#     self.alias = alias
#     self.kelompok = kelompok
#     self.listHero = listHero
 
# listHero = []
# for i in range(5) : 
#     nama = input('\nmasukan nama : ')
#     alias = input('masukan nama alias : ')
#     kelompok = input('masukan kelompok : ')
#     listHero.append(Hero(nama,alias,kelompok))

# print ("Hero pertama:", listHero[0].nama,"\n")
# print("Daftar superhero:\n")
# for Hero in listHero:
#     print("\nNama: {}\nAlias: {}\nKelompok: {}\n\n".format(Hero.nama, Hero.alias, Hero.kelompok))


import tkinter as tk
master = tk.Tk()

class Hero(object):
    def __init__(self, nama=None, alias=None, kelompok=None, list_hero=None):
        self.nama = nama
        self.alias = alias
        self.kelompok = kelompok
        self.listHero = listHero
    
    tk.Label(master, text='nama : ').grid(row=0)
    tk.Label(master, text='alias : ').grid(row=1)
    tk.Label(master, text='kelompok : ').grid(row=2)

    n = tk.Entry(master)
    a = tk.Entry(master)
    k = tk.Entry(master)

    n.grid(row=0, column=2)
    a.grid(row=1, column=2)
    k.grid(row=2, column=2) 

    def hero() :
        txt_nama = 'nama : %s'%(n.get())
        txt_alias = 'alias : %s'%(a.get())
        txt_kelom = 'kelompok : %s'%(k.get())
        tk.Label(master, text=txt_nama).grid(row=4, columnspan=2)
        tk.Label(master, text=txt_alias).grid(row=5, columnspan=2)
        tk.Label(master, text=txt_kelom).grid(row=6, columnspan=2)

    tampil = tk.Button(master, text='tampil', command=hero)
    tampil.grid(row=3, column=0, sticky=tk.W, pady=4)

    tk.mainloop()

 