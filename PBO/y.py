class pegawai :
    def __init__(self):
        self.nip = ''
        self.nama = ''
        self.jabatan = ''
        self.gaji_pokok = ''
        self.tunjangan = ''
        self.pajak = ''
        
    def ubah_jabatan(self) :
        self.nip = input('\nmasukan nip : ')
        setattr(pegawai, 'nip', self.nip)
        self.nama = input('masukan nama : ')
        setattr(pegawai, 'nama', self.nama)
        self.jabatan = input('masukan jabatan : ')
        setattr(pegawai, 'jabatan', self.jabatan)
        self.gaji_pokok =int(input('masukan gaji pokok : '))
        setattr(pegawai, 'gaji_pokok', self.gaji_pokok)
        self.tunjangan = int(input('masukan tunjangan : '))
        setattr(pegawai, 'tunjangan', self.tunjangan)
        self.pajak = int(input('masukan pajak : '))
        setattr(pegawai, 'pajak', self.pajak)
    def ubah_gaji_pokok(self) :
        self.gaji_pokok = int(input('masukan gaji pokok : '))
        setattr(pegawai, 'gaji_pokok', self.gaji_pokok)
    def gaji_bersih(self) :
        a = self.gaji_pokok
        b = self.tunjangan
        c = self.pajak
        gaji_bersih = a+b-c
        print('gaji bersih pegawai : ', gaji_bersih)
    def tampil(self) :
        print('nip : ', getattr(pegawai, 'nip'))
        print('nama : ', getattr(pegawai, 'nama'))
        print('jabatan : ', getattr(pegawai, 'jabatan'))
        print('gaji pokok : ', getattr(pegawai, 'gaji_pokok'))
        print('tunjangan : ', getattr(pegawai, 'tunjangan'))
        print('pajak : ', getattr(pegawai, 'pajak'))

class sekretaris(pegawai) : 
    def __init__(self) :
        self_upahlembur = None
    def ubah_upah(self):
        self.upahlembur = int(input('masukan upah lembur : '))
    def gaji_brs(self) :
        a = self.gaji_pokok
        b = self.tunjangan
        c = self.pajak
        d = self.upahlembur
        gaji_brs = (a+b+d)-c
        print('gaji bersih : ', gaji_brs)
    def tmpl(self) :
        print('upah lembur : ', self.upahlembur)

class manajer(pegawai) :
    def __init__(self) :
        self.bonus = None
    def ubah_bonus(self) :
        self.bonus = int(input('masukan bonus : '))
    def gaji_brsh(self) :
        a = self.gaji_pokok
        b = self.tunjangan
        c = self.pajak
        d = self.bonus
        gaji_brsh = (a+b+d)-c
        print('gaji bersih : ', gaji_brsh)
    def tmp(self) :
        print('bonus : ', self.bonus)

skr = sekretaris()
mnj = manajer()

while True :
    skr.ubah_jabatan()
    print('\nTAMPIL DATA PEGAWAI')
    skr.tampil()
    skr.gaji_bersih()

    print('\nPILIH DATA DIBAWAH')
    print('1. Sekretaris')
    print('2. Manajer')
    print('3. Keluar')

    pilihan = int(input('masukan pilihan : '))

    if pilihan == 1 :
        skr.ubah_upah()
        print('\nSEKRETARIS')
        skr.tmpl()
        skr.gaji_brs()

        print('\nDATA YANG MAU DIUBAH')
        print('1. ubah gaji pokok')
        print('2. ubah upah')
        print('3. keluar')

        pilihan = int(input('masukan pilihan : '))

        if pilihan == 1 : 
            skr.ubah_gaji_pokok()
            print('\nSEKRETARIS')
            skr.tmpl()
            skr.gaji_brs()
        elif pilihan == 2 :
            skr.ubah_upah()
            print('\nSEKRETARIS')
            skr.tmpl()
            skr.gaji_brs()
        else :
            print('KELUARR')
    elif pilihan == 2 :
        mnj.ubah_bonus()
        print('\nMANAJER')
        mnj.tmp()
        mnj.gaji_brsh()

        print('\nDATA YANG MAU DIUBAH')
        print('1. ubah gaji pokok')
        print('2. ubah bonus')
        print('3. keluar')

        pilihan = int(input('masukan pilihan : '))

        if pilihan == 1 :
            mnj.ubah_gaji_pokok()
            print('\nMANAJER')
            mnj.tmp()
            mnj.gaji_brsh()
        elif pilihan == 2 :
            mnj.ubah_bonus()
            print('\nMANAJER')
            mnj.tmp()
            mnj.gaji_brsh()
        else :
            print('KELUARRR')
    else : 
        print('KELUARRRRR')
        break


