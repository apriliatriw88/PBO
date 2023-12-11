# from abc import ABC, abstractmethod

# class artis(ABC) :
#     @abstractmethod
#     def bidang(self) :
#         pass

# class penyanyi(artis) :
#     def bidang(self) :
#         print('nyanyi pop')

# class pemainFilm(artis) :
#     def bidang(self) :
#         print('film horror')

# p = penyanyi()
# p.bidang()

# f = pemainFilm()
# f.bidang()

# class ortu :
#     def __init__(self) :
#         self.sikap = ''
#         self.agama =''
#     def InputDataOrtu(self) :
#         print('\nMasukan data dengan benar')
#         print('\n======DATA ORTU======')
#         self.sikap = input('masukan sikap : ')
#         setattr(ortu, 'sikap', self.sikap)
#         self.agama = input('masukan agama : ')
#         setattr(ortu, 'agama', self.agama)
#     def TampilDataOrtu(self) :
#         print('sikap : ', getattr(ortu, 'sikap'))
#         print('agama : ', getattr(ortu, 'agama'))

# class guru :
#     def __init__(self) :
#         self.ilmu = ''
#     def InputDataGuru(self) :
#         print('\n======DATA GURU=====')
#         self.ilmu = input('masukan ilmu : ')
#         setattr(guru, 'ilmu', self.ilmu)
#     def TampilDataGuru(self) :
#         print('ilmu : ', getattr(guru, 'ilmu'))

# class murid(ortu, guru) :
#     def __init__(self) :
#         self.nama = None
#         self.__umur = None
#         self.kelas = None
#         ortu.__init__(self)
#         guru.__init__(self)
#     def InputDataAnak(self) :
#         print()
#         self.nama = input('masukan nama : ')
#         self.__umur = input('masukan umur : ')
#         self.kelas = input('masukan kelas : ')
#     def TampilDataAnak(self) :
#         print('\nDATA MURID')
#         ortu.TampilDataOrtu(self)
#         guru.TampilDataGuru(self)
#         print('nama : ', self.nama)
#         print('umur : ', self.__umur)
#         print('kelas : ', self.kelas)

# mr = murid()
# mr.InputDataOrtu()
# mr.InputDataGuru()
# mr.InputDataAnak()
# mr.TampilDataAnak()

class orang :
    def __init__(self) :
        self.nama = ''
        self.id = ''
        self.jenis_kelamin = ''
        self.no_telepon = ''
    def input_data (self) :
        self.nama = input('\nmasukan nama : ')
        self.id = input('masukan id : ')
        self.jenis_kelamin = input('masukan jenis kelamin : ')
        try :
            self.no_telepon = input('masukan no telepon : ')
        except :
            print('harus angka')
    def tampil_data (self) :
        print('nama : ', self.nama)
        print('id : ', self.id)
        print('jenis kelamin : ', self.jenis_kelamin)
        print('no telepon : ', self.no_telepon)
    def ubah_data_diri (self):
        self.nama = input('\nmasukan nama : ')
        self.id = input('masukan id : ')
        self.jenis_kelamin = input('masukan jenis kelamin : ')
        try :
            self.no_telepon = int(input('masukan no telepon : '))
        except :
            print('harus angka')

    def hapus_data_diri (self):
        delattr(orang, 'nama')
        delattr(orang, 'id')
        delattr(orang, 'jenis_kelamin')
        delattr(orang, 'no_telepon')

class tugas :
    def __init__(self) :
        self.id = ''
        self.nama_tugas = ''
        self.tanggal_mulai = ''
        self.tanggal_selesai = ''
        self.status_tugas = ''
    def input_dataa(self) :
        self.id = input('\nmasukan id : ')
        self.nama_tugas = input('masukan nama tugas : ')
        self.tanggal_mulai = input('masukan tanggal mulai : ')
        self.tanggal_selesai = input('masukan tanggal selesai : ')
        self.status_tugas = input('masukan status tugas : ')
    def tampil_dataa(self) :
        print('id : ', self.id)
        print('nama tugas : ', self.nama_tugas)
        print('tanggal mulai : ', self.tanggal_mulai)
        print('tanggal selesai : ', self.tanggal_selesai)
        print('status tugas : ', self.status_tugas)
    def ubah_tugass(self) : 
        self.id = input('\nmasukan id : ')
        self.nama_tugas = input('masukan nama tugas : ')
        self.tanggal_mulai = input('masukan tanggal mulai : ')
        self.tanggal_selesai = input('masukan tanggal selesai : ')
        self.status_tugas = input('masukan status tugas : ')
    def hapus_tugas(self) :
        delattr(tugas, 'id')
        delattr(tugas, 'nama_tugas')
        delattr(tugas, 'tanggal_mulai')
        delattr(tugas, 'tanggal_selesai')
        delattr(tugas, 'status_tugas')
    
class PelacakTugas(orang, tugas) :
    def __init__(self) :
        self.penanggungjawab = None
        orang.__init__(self)
        tugas.__init__(self)
    def input_dataaa(self) :
        self.penanggungjawab = input('\nmasukan penanggung jawab : ')
    def tampil_data_tugas(self) :
        print('penanggung jawab : ', self.penanggungjawab)
    def tampil_detail_tugas (self) :
        orang.tampil_data(self)
        tugas.tampil_dataa(self)
        print('\npenanggung jawab : ', self.penanggungjawab)
    def ubah_tugas (self) :
        self.penanggungjawab = input('\nmasukan penanggung jawab : ')
    def hapus_tugas (self) :
        delattr(PelacakTugas, 'penanggungjawab')

p = PelacakTugas()
p.input_data()
p.tampil_data()


p.input_dataa()
p.tampil_dataa()


p.input_dataaa()
p.tampil_data_tugas()
p.tampil_detail_tugas()




