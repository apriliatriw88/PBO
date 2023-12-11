
print('SET')
# set data campuran 
data = {1, 2.0, "jarvis", (3,4,5)} 
print('Set gabungan: ',data) 

# bila kita mengisi duplikasi, set akan menghilangkan salah satu
# output: {1,2,3} 
angka = {1,2,2,3,3,3} 
print('Set angka:',angka) 

# set tidak bisa berisi anggota list 
# contoh berikut akan muncul error TypeError 
# set_baru = {1,2,[3,4,5]} 
# supaya bisa program bisa jalan, baris diatas dikomen atau dihapus

# menambah anggota baru pada set angka
angka.add(4) 
print('Set angka perubahan 1:',angka)

# menambah beberapa anggota sekaligus
angka.update([3,4,5,6]) 
print('Set angka perubahan 2:',angka)

# mengosongkan set
angka.clear()
print('Set angka perubahan 3:',angka)

print('\nOperasi himpunan matematika')
# Membuat set A and B 
A = {1, 2, 3, 4, 5} 
B = {4, 5, 6, 7, 8} 
print('A:',A)
print('B:',B)

# Gabungan menggunakan operator | 
print('A gabung B: ',(A | B))

# Irisan menggunakan operator & 
print('A irisan B: ',(A & B))

# operasi selisih
print('A - B: ',(A - B))
# operasi komplemen

print('A komplemen B: ',(A ^ B))