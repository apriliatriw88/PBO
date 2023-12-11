print('_'*30,'KELOMPOK 9','_'*30)
print('''\n1. Aprilia Tri Widiyastuti(212103005)
2. Anta Khosiya Rohmana   (212103004)
3. Muh.Alvisyahr          (212103031)''')
print()

from abc import ABC,abstractmethod

class Laundry(ABC):
    @abstractmethod
    def __init__(self):
        pass
    @abstractmethod
    def Input_Data(self):
        pass
    @abstractmethod
    def Tampil_Data(self):
        pass

class Akun:
    def __init__(self):
        self.Daftar_Email=[]
        self.Daftar_Password=[]
        self.Input_Email=None
        self.Input_Password=None

    def Register_Login(self):     
        print('\t\t>---Daftarkan Email Dan Password Anda---<')
        self.Daftar_Email.append(input('\n\t\t        Daftarkan Email   : '))
        self.Daftar_Password.append(input('\t\t        Daftarkan Password: '))
        print('\t               AKUN BERHASIL TERDAFTAR')
        while True:
            tanya=input('\nDaftarkan Akun Lagi (Yes/No)? ')
            if tanya == 'Yes':
                Akun.Register(self)
            elif tanya== 'No':
                print('\n\t\t>---Masukkan Email Dan Password Anda---<')
                self.Input_Email=input('\n\t\t\tMasukkan Email   : ')
                El=self.Input_Email in self.Daftar_Email
                if El ==True:
                    self.Input_Password=input('\t\t\tMasukkan Password: ')
                    Pw=self.Input_Password in self.Daftar_Password
                    if Pw ==True:
                        print('\t                 ANDA BERHASIL LOGIN\n')
                        break                  
                    else: 
                       print('\t\tPassword Yang Anda Masukkan Salah')
                else:
                    print('\t\tEmail Tidak Tersedia')
            else:
                print('\t\tPilihan Tidak Tersedia')
         
class Pelanggan:
    def __init__(self):
        self.Nama_pelanggan= None
        self.Id_pelanggan= None
        self.Alamat=None
        self.__Nomor_Telephone=None
    def Input_Data(self):
        self.Nama_pelanggan=input('\tMasukkan Nama Anda   : ')
        self.Id_pelanggan=input('\tMasukkan Id Pelanggan: ')
        self.Alamat=input('\tMasukkan Alamat      : ')
        self.__Nomor_Telephone=input('\tMasukkan No Hp       : ')
        teks= '''\tNama Pelanggan           :  {}\n\tId pelanggan             :  {}\n\tAlamat                   :  {}\n\tNo Hp                    :  {}'''.format(self.Nama_pelanggan, self.Id_pelanggan, self.Alamat, self.__Nomor_Telephone)
        file_bio = open("tb.txt", "w")
        file_bio.write(teks)
        file_bio.close() 
    def Tampil_Data(self):
        file_puisi = open("tb.txt", "r")
        puisi = file_puisi.read()
        print (puisi)            
        file_puisi.close()


class Transaksi:
    def __init__(self):
        self.Layanan_Antar_jemput= 0
        self.Berat_pakaian= None
        self.Jumlah= None
        self.Diskon= None
        self.Uang=None
        self.Total_Harga=None
    def Input_Data(self):
        self.Berat_pakaian=int(input('\tMasukkan Berat Pakaian (Kg)/ satuan(pcs)               : '))
        setattr(Transaksi,'btp',self.Berat_pakaian)
        self.pilihan_layanan=input('\tApakah Anda Ingin Menambahkan Layanan Antar Jemput[Y/N]: ')
        print('~'*90)
    def Tampil_Data(self):
        print('\tJasa Layanan Antar Jemput:  Rp.',self.Layanan_Antar_jemput)
        print('\tBerat Pakaian            : ',getattr(Transaksi,'btp'),'Kg/Pcs')
        print('\tTotal Sementara          :  Rp.',self.Jumlah)
        self.Total_Harga=self.Jumlah
        if self.Jumlah>50000:
            self.Diskon=self.Jumlah*10/100
            print('\tDiskon                   :  Rp.',self.Diskon)
            self.Total_Harga=self.Jumlah-self.Diskon
        print('\tTotal Harga              :  Rp.',self.Total_Harga)
        print('~'*90)
        self.Uang=int(input('\tMasukkan Uang Pembayaran : Rp.'))
        if self.Uang>self.Total_Harga:
            print('\tKembaliannya             : Rp.',self.Uang-self.Total_Harga)          
        elif self.Uang == self.Total_Harga:
            print('\tUang Anda Pas')
        else: 
            self.Uang_kurang=print('\tUang Anda Kurang Sebesar : Rp.',self.Uang-self.Total_Harga)
            input('\tMasukkan Uang Yang Kurang: Rp.')

class Jenis(Laundry,Pelanggan,Transaksi):
    def __init__(self):
        self.Paket_Express= 12000
        self.Paket_Reguler= 8000
        self.Cuci_Kering_Express= 7000
        self.Cuci_Kering_Biasa= 5000
        self.Bedcover_Express= 30000
        self.Bedcover_Biasa= 20000
        self.Helm= 25000
        self.Tgl_Transaksi= None
        self.Kode_Layanan=None
        self.Id_Laundry=None
    def Input_Data(self):
        self.Kode_Layanan=int(input('\tMasukkan Kode Layanan[1-7]                             : '))  
        setattr(Jenis,'kl',self.Kode_Layanan)
        self.Tgl_Transaksi=input('\tMasukkan Tanggal Transaksi                             : ')
        setattr(Jenis,'tgl',self.Tgl_Transaksi) 
        self.Id_Laundry=input('\tMasukkan Id Laundry                                    : ')
        setattr(Jenis,'idl',self.Id_Laundry)
    def Tampil_Data(self):
        if self.Kode_Layanan==1:
            Transaksi.Input_Data(self)
            if self.pilihan_layanan=='Y':
                self.Layanan_Antar_jemput=5000
                self.Jumlah= self.Berat_pakaian*self.Paket_Express + self.Layanan_Antar_jemput
            elif self.pilihan_layanan=='N':
                self.Jumlah= self.Berat_pakaian*self.Paket_Express 
            Pelanggan.Tampil_Data(self)
            print('\tTanggal Transaksi        : ',getattr(Jenis,'tgl'))
            print('\tId laundry               : ',getattr(Jenis,'idl'))
            print('\tKode Layanan             : ',getattr(Jenis,'kl'))
            print('\tJenis Layanan            :  Paket Express (1 Hari)')
            print('\tHarga                    :  Rp.',self.Paket_Express)
            Transaksi.Tampil_Data(self)

        elif self.Kode_Layanan==2:
            Transaksi.Input_Data(self)
            if self.pilihan_layanan=='Y':
                self.Layanan_Antar_jemput=5000
                self.Jumlah= self.Berat_pakaian*self.Paket_Reguler + self.Layanan_Antar_jemput
            elif self.pilihan_layanan=='N':
                self.Jumlah= self.Berat_pakaian*self.Paket_Reguler 
            Pelanggan.Tampil_Data(self)
            print('\tTanggal Transaksi        : ',getattr(Jenis,'tgl'))
            print('\tId laundry               : ',getattr(Jenis,'idl'))
            print('\tKode Layanan             : ',getattr(Jenis,'kl'))
            print('\tJenis Layanan            :  Paket Reguler (2 Hari)')
            print('\tHarga                    :  Rp.',self.Paket_Reguler)
            Transaksi.Tampil_Data(self)

        elif self.Kode_Layanan==3:
            Transaksi.Input_Data(self)
            if self.pilihan_layanan=='Y':
                self.Layanan_Antar_jemput=5000
                self.Jumlah= self.Berat_pakaian*self.Cuci_Kering_Express + self.Layanan_Antar_jemput
            elif self.pilihan_layanan=='N':
                self.Jumlah= self.Berat_pakaian*self.Cuci_Kering_Express 
            Pelanggan.Tampil_Data(self)
            print('\tTanggal Transaksi        : ',getattr(Jenis,'tgl'))
            print('\tId laundry               : ',getattr(Jenis,'idl'))
            print('\tKode Layanan             : ',getattr(Jenis,'kl'))
            print('\tJenis Layanan            :  Paket Cuci kering Express')
            print('\tHarga                    :  Rp.',self.Cuci_Kering_Express)
            Transaksi.Tampil_Data(self)

        elif self.Kode_Layanan==4:
            Transaksi.Input_Data(self)
            if self.pilihan_layanan=='Y':
                self.Layanan_Antar_jemput=5000
                self.Jumlah= self.Berat_pakaian*self.Cuci_Kering_Biasa + self.Layanan_Antar_jemput
            elif self.pilihan_layanan=='N':
                self.Jumlah= self.Berat_pakaian*self.Cuci_Kering_Biasa 
            Pelanggan.Tampil_Data(self)
            print('\tTanggal Transaksi        : ',getattr(Jenis,'tgl'))
            print('\tId laundry               : ',getattr(Jenis,'idl'))
            print('\tKode Layanan             : ',getattr(Jenis,'kl'))
            print('\tJenis Layanan            :  Paket Cuci kering Biasa')
            print('\tHarga                    :  Rp.',self.Cuci_Kering_Biasa)
            Transaksi.Tampil_Data(self)

        elif self.Kode_Layanan==5:
            Transaksi.Input_Data(self)
            if self.pilihan_layanan=='Y':
                self.Layanan_Antar_jemput=5000
                self.Jumlah= self.Berat_pakaian*self.Bedcover_Express + self.Layanan_Antar_jemput
            elif self.pilihan_layanan=='N':
                self.Jumlah= self.Berat_pakaian*self.Bedcover_Express
            Pelanggan.Tampil_Data(self)
            print('\tTanggal Transaksi        : ',getattr(Jenis,'tgl'))
            print('\tId laundry               : ',getattr(Jenis,'idl'))
            print('\tKode Layanan             : ',getattr(Jenis,'kl'))
            print('\tJenis Layanan            :  Bedcover Express')
            print('\tHarga                    :  Rp.',self.Bedcover_Express)
            Transaksi.Tampil_Data(self)

        elif self.Kode_Layanan==6:
            Transaksi.Input_Data(self)
            if self.pilihan_layanan=='Y':
                self.Layanan_Antar_jemput=5000
                self.Jumlah= self.Berat_pakaian*self.Bedcover_Biasa + self.Layanan_Antar_jemput
            elif self.pilihan_layanan=='N':
                self.Jumlah= self.Berat_pakaian*self.Bedcover_Biasa
            Pelanggan.Tampil_Data(self)
            print('\tTanggal Transaksi        : ',getattr(Jenis,'tgl'))
            print('\tId laundry               : ',getattr(Jenis,'idl'))
            print('\tKode Layanan             : ',getattr(Jenis,'kl'))
            print('\tJenis Layanan            :  Bedcover Biasa')
            print('\tHarga                    :  Rp.',self.Bedcover_Biasa)
            Transaksi.Tampil_Data(self)

        elif self.Kode_Layanan==7:
            Transaksi.Input_Data(self)
            if self.pilihan_layanan=='Y':
                self.Layanan_Antar_jemput=5000
                self.Jumlah= self.Berat_pakaian*self.Helm + self.Layanan_Antar_jemput
            elif self.pilihan_layanan=='N':
                self.Jumlah= self.Berat_pakaian*self.Helm
            Pelanggan.Tampil_Data(self)
            Laundry.Tampil_Data(self)
            print('\tTanggal Transaksi        : ',getattr(Jenis,'tgl'))
            print('\tId laundry               : ',getattr(Jenis,'idl'))
            print('\tKode Layanan             : ',getattr(Jenis,'kl'))
            print('\tJenis Layanan            :  Helm')
            print('\tHarga                    :  Rp.',self.Helm)
            Transaksi.Tampil_Data(self)
        
A=Akun()
A.Register_Login()
png=Pelanggan()
jns=Jenis()
while True:
    print('\n\t\t\t{________________{MENU UTAMA}________________}')
    print('''
              \t\t\t     1. Jenis Laundry
              \t\t\t     2. Catat Transaksi
              \t\t\t     3. Keluar Program ''')

    pilihan=int(input('\t\t\t\t     Masukkan Pilihan Anda: '))
    print()

    if pilihan==1:
        print('''
        |*******************************************************************************|
        |                        DAFTAR PAKET JENIS LAYANAN LAUNDRY                     |
        |*******************************************************************************|
        |  Kode  |                  Jenis Layanan                    |      Harga       |  
        |*******************************************************************************|
        |    1   |             Paket Express (1 Hari)                |   Rp. 12.000/Kg  |
        |    2   |             Paket Reguler (2 Hari)                |   Rp. 8.000/Kg   |
        |    3   |            Paket Cuci Kering Express              |   Rp. 7.000/Kg   | 
        |    4   |             Paket Cuci Kering Biasa               |   Rp. 5.000/Kg   |
        |    5   |               Bedcover Express                    |   Rp. 30.000/pcs |
        |    6   |                Bedcover Biasa                     |   Rp. 20.000/pcs |
        |    7   |                    Helm                           |   Rp. 25.000/pcs |         
        |*******************************************************************************|
        
        |*******************************************************************************|
        |  NOTE:                                                                        |
        |        Jika Total Sementara lebih dari 50rb maka mendapatkan diskon 10%       |
        |        Jika anda memilih layanan antar jemput maka tambah biaya Rp 5.000      |
        |*******************************************************************************|''')

    elif pilihan==2:
        
        print('''Silahkan Memilih:
        1. Tambah Pelanggan
        2. Lihat Pelanggan
        3. Transaksi ''')

        pil=int(input('Masukkan Pilihan Anda: '))
        print()
        if pil==1:
            print('\n+','='*50,'+')                                    
            print('|\t           TAMBAH PELANGGAN                  |')
            print('+','='*50,'+')
            png.Input_Data()
            print('+','='*50,'+')

        elif pil==2:
            print('\n+','='*50,'+')                                    
            print('|\t           LIHAT PELANGGAN                   |')
            print('+','='*50,'+')
            file_puisi = open("tb.txt", "r")
            puisi = file_puisi.read()
            print (puisi)
            file_puisi.close()
            print('+','='*50,'+')
            
        elif pil==3:
            print('\t\t\t    STRUCK NOTA | | LAUNDRY')
            print('~'*90)
            jns.Input_Data()
            jns.Tampil_Data()
            print('~'*90)
            print('\t','~'*30,'TRANSAKSI SELESAI','~'*30)
            
            lanjut=input('Apakah Anda Ingin Melanjutkan Program[Y/N]: ')
            if lanjut=='Y':
                pass
            elif lanjut=='N':
                print('ANDA KELUAR DARI PROGRAM')
                break
        else:
            print('\tPILIHAN ANDA TIDAK TERSEDIA')
            break
    
    else:
        print('\t\t\t\t\t',">" * 15)
        print('\t\t\t\t\t',"|  THANK YOU  |")
        print('\t\t\t\t\t',">" * 15)
        break


            
            









