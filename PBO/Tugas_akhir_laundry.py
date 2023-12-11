from tkinter.messagebox import showerror, showinfo
import tkinter as tk
import sqlite3
from tkinter.ttk import Combobox,Treeview

Laundry=tk.Tk()

from abc import ABC,abstractmethod
# class Abstrack(ABC):
class Login(ABC): 
    def __init__(self):
        self.Email=[]
        self.__Password=[]
        Login.login_register(self)

    @abstractmethod
    def Laundry(self):
        pass
              
    def login_register(self):
        Laundry.title('Login And Register')
        Laundry.geometry('400x200')
        Laundry.configure(bg='pink')
        
        self.Teks=tk.Label(Laundry,text="...LAUNDRY...",bg='pink',font='Heltevica  25 bold italic')
        self.Teks.place(x=100,y=0) 

        Teks_email=tk.Label(Laundry,text='Email',bg='pink',font='arial 10 bold')
        Teks_email.place(y=70,x=100)
        Entry_email=tk.Entry(Laundry,bd=3)
        Entry_email.place(y=70,x=150)

        Teks_pw=tk.Label(Laundry,text='Password',bg='pink',font='arial 10 bold')
        Teks_pw.place(y=100,x=80)
        Entry_pw=tk.Entry(Laundry,bd=3)
        Entry_pw.place(x=150,y=100)

        def login():
            if Entry_email.get() in self.Email and Entry_pw.get() in self.__Password:
                showinfo(title="Login", message="Login Berhasil")
                Menu.Laundry(self) 
                Entry_email.delete(0,tk.END)
                Entry_pw.delete(0,tk.END)
            elif Entry_email.get() in self.Email and Entry_pw.get() not in self.__Password:
                showinfo(title="Info", message="Password Yang Anda Masukkan Salah")
            elif Entry_email.get()=='' and Entry_pw.get()=='':
                showinfo(title="Info", message="Anda Harus Mengisi Email Dan Pasword Jika Ingin Login")
            else:
                showinfo(title="Info", message="Akun Yang Anda Masukkan Belum Terdaftar")
        
        Button_login=tk.Button(Laundry,text='LOGIN',bg='SteelBlue2',fg='white',relief='solid',font='Helvetica 10 bold',command=login)
        Button_login.place(x=25,y=160)
        Button_login.config(height=1,width=20)

        def register():
            if Entry_email.get()=='' and Entry_pw.get()=='':
                showinfo(title="Info", message="Anda Harus Mengisi Email Dan Pasword Jika Ingin Melakukan Register") 
            elif Entry_email.get()==Entry_email.get() and Entry_pw.get()=='':
                showinfo(title="Info", message="Anda Harus Mengisi Keduanya") 
            elif Entry_email.get()=='' and Entry_pw.get()==Entry_pw.get():
                showinfo(title="Info", message="Anda Harus Mengisi Keduanya")
            else:
                self.Email.append(Entry_email.get())
                self.__Password.append(Entry_pw.get())
                print(self.Email,self.__Password)
                showinfo(title="Register", message="Selamat Akun Anda Berhasil Terdaftar")
                Entry_email.delete(0,tk.END)
                Entry_pw.delete(0,tk.END)
        
        Button_register=tk.Button(Laundry,text='REGISTER',bg='SteelBlue2',fg='white',relief='solid',font='Helvetica 10 bold',command=register)
        Button_register.place(x=200,y=160)
        Button_register.config(height=1,width=20)
    
class Jenis():
    def __init__(self):
        self.Teks3=None
        self.tree=None
        self.Frame=None
        self.Teks_note=None
        self.kembali=None
        self.Tombol_jenis_laundry=None
              
    def Laundry(self):
            Laundry3=tk.Toplevel()
            Laundry3.geometry('700x400')
            Laundry3.title('Jenis Laundry')
            Laundry3.configure(bg='pink')
    
            self.Teks2=tk.Label(Laundry3,text="...LAUNDRY...",bg='pink',font='Heltevica  35 bold italic')
            self.Teks2.place(x=200,y=0)

            self.Teks3=tk.Label(Laundry3,text="..Jenis Laundry..",bg='pink',font='Courier  15 bold')
            self.Teks3.place(x=250,y=50)

            self.tree=Treeview(Laundry3,columns=('#0','#1'))
            self.tree.heading('#0', text='No')
            self.tree.heading('#1', text='Jenis Layanan')
            self.tree.heading('#2', text='Harga')

            self.tree.column('#0',width=10,minwidth=50)
            self.tree.column('#1',minwidth=100)
            self.tree.grid(row=0,columnspan=1,pady=100,padx=150,sticky='nsew')
            self.tree.config(height=7)

            self.tree.insert('','end',text='1',values=('Paket Express (1 Hari)','Rp. 12.000/Kg'))
            self.tree.insert('','end',text='2',values=('Paket Reguler (2 Hari)','Rp. 8.000/Kg'))
            self.tree.insert('','end',text='3',values=('Paket Cuci Kering Express','Rp. 7.000/Kg'))
            self.tree.insert('','end',text='4',values=('Paket Cuci Kering Biasa','Rp. 5.000/Kg'))
            self.tree.insert('','end',text='5',values=('Bedcover Express','Rp. 30.000/pcs'))
            self.tree.insert('','end',text='6',values=('Bedcover Biasa','Rp. 20.000/pcs'))
            self.tree.insert('','end',text='7',values=('Helm','Rp. 25.000/pcs'))

            self.Frame = tk.LabelFrame(Laundry3,bd=5)
            self.Frame.place(x=150,y=266)
           
            self.Teks_note=tk.Label(self.Frame,text='''NOTE:
            Jika anda memilih layanan antar jemput maka tambah biaya Rp 5.000
            Jika jumlah lebih dari 100.000 rb maka mendapatkan diskon 15%''')
            self.Teks_note.grid()

            def back():
                Menu.Laundry(self)
                Laundry3.destroy()
            self.kembali=tk.Button(Laundry3,text='Back',command=back,relief='groove',width=10,font='verdana  8 bold ',background='silver',fg='black')
            self.kembali.place(x=470,y=350)

class Transaksi():
    def __init__(self):
        self.Paket_Express= 12000
        self.Paket_Reguler= 8000
        self.Cuci_Kering_Express= 7000
        self.Cuci_Kering_Biasa= 5000
        self.Bedcover_Express= 30000
        self.Bedcover_Biasa= 20000
        self.Helm= 25000
        Transaksi.Laundry(self)
    
    def Laundry(self):
            Laundry4=tk.Toplevel()
            Laundry4.geometry('1200x600') 
            Laundry4.title('Transaksi Laundry')
            Laundry4.configure(bg='pink')

            self.Teks5=tk.Label(Laundry4,text="...LAUNDRY...",bg='pink',font='Heltevica  35 bold italic')
            self.Teks5.place(x=450,y=0)

            self.Teks6=tk.Label(Laundry4,text="Transaksi Laundry",bg='pink',font='Courier  15 bold')
            self.Teks6.place(x=500,y=60)

            self.labelframe1 = tk.LabelFrame(Laundry4, text="Data Transaksi",bg='pink',bd=5)#bg='silver')
            self.labelframe1.place(x=0,y=85)
            self.labelframe1.grid_propagate(0)
            self.labelframe1.config(width=620,height=230)

            self.labelframe2 = tk.LabelFrame(Laundry4,bg='pink',bd=5)
            self.labelframe2.place(x=615,y=90)
            self.labelframe2.grid_propagate(0)
            self.labelframe2.config(width=590,height=230)

            self.Teks_nama=tk.Label(self.labelframe1,text="NAMA",bg='pink',padx=5,pady=0)
            self.Teks_nama.grid(column=1,row=0,sticky='W')
            self.Entry_nama=tk.Entry(self.labelframe1,width=30,bd=1)
            self.Entry_nama.grid(column=50,row=0,padx=50,pady=0)

            self.Teks_alamat=tk.Label(self.labelframe1,text="ALAMAT",bg='pink',padx=5,pady=0)
            self.Teks_alamat.grid(column=1,row=2,sticky='W')
            self.Entry_alamat=tk.Entry(self.labelframe1,width=30,bd=1)
            self.Entry_alamat.grid(column=50,row=2,padx=153,pady=0)
    
            self.Teks_no_hp=tk.Label(self.labelframe1,text="NO HP",bg='pink',padx=5,pady=0)
            self.Teks_no_hp.grid(column=1,row=3,sticky='W')
            self.Entry_no_hp=tk.Entry(self.labelframe1,width=30,bd=1)
            self.Entry_no_hp.grid(column=50,row=3,padx=153,pady=0)
              
            self.Teks_jenis=tk.Label(self.labelframe1,text="JENIS LAUNDRY",bg='pink',padx=5,pady=0)
            self.Teks_jenis.grid(column=1,row=4,sticky='W')
            
            self.Pilihan_jenis=['Pilih Jenis','Paket Express (1 Hari)','Paket Reguler (2 Hari)','Paket Cuci Kering Express','Paket Cuci Kering Biasa','Bedcover Express','Bedcover Biasa','Helm']
            self.Box_jenis=Combobox(self.labelframe1,values=self.Pilihan_jenis,width=27)
            self.Box_jenis.grid(column=50,row=4,padx=95,pady=0)
            self.Box_jenis.current(0)

            self.Teks_tgl_transaksi=tk.Label(self.labelframe1,text="TANGGAL TRANSAKSI",bg='pink',padx=5,pady=0)
            self.Teks_tgl_transaksi.grid(column=1,row=6,sticky='W')
            self.Entry_tgl_transaksi=tk.Entry(self.labelframe1,width=30,bd=1)
            self.Entry_tgl_transaksi.grid(column=50,row=6,padx=95,pady=0)

            self.Teks_id_laundry=tk.Label(self.labelframe1,text="ID LAUNDRY",bg='pink',padx=5,pady=0)
            self.Teks_id_laundry.grid(column=1,row=7,sticky='W')
            self.Entry_id_laundry=tk.Entry(self.labelframe1,width=30,bd=1)
            self.Entry_id_laundry.grid(column=50,row=7,padx=95,pady=0)

            self.Teks_berat_pakaian=tk.Label(self.labelframe1,text="BERAT PAKAIAN",bg='pink',padx=5,pady=0)
            self.Teks_berat_pakaian.grid(column=1,row=8,sticky='W')
            self.Entry_berat_pakaian=tk.Entry(self.labelframe1,width=30,bd=1)
            self.Entry_berat_pakaian.grid(column=50,row=8,padx=95,pady=0)

            self.Teks_layanan_antar_jemput=tk.Label(self.labelframe1,text="LAYANAN ANTAR JEMPUT",bg='pink',padx=5,pady=0)
            self.Teks_layanan_antar_jemput.grid(column=1,row=9,sticky='W')
            
            self.Pilihan_antar_jemput=['Pilih Layanan','No','Yes',]
            self.Box_antar_jemput=Combobox(self.labelframe1,values=self.Pilihan_antar_jemput,width=27)
            self.Box_antar_jemput.grid(column=50,row=9,padx=95,pady=0)
            self.Box_antar_jemput.current(0)

            self.Teks_status=tk.Label(self.labelframe1,text="STATUS",bg='pink',padx=5,pady=0)
            self.Teks_status.grid(column=1,row=10,sticky='W')
            self.Pilihan_status=['Pilih Status','Lunas','Belum Bayar']
            self.Box_status=Combobox(self.labelframe1,values=self.Pilihan_status,width=27)
            self.Box_status.grid(column=50,row=10,padx=95,pady=0)
            self.Box_status.current(0)
           
            self.labelframe3 = tk.LabelFrame(Laundry4,bd=5)
            self.labelframe3.place(y=300)
            self.labelframe3.config(height=1)

            self.tree2=Treeview(self.labelframe3,columns=('#0','#1','#2','#3','#4','#5','#6','#7','#9','#10','#11'))
            self.tree2.heading('#0', text='Nama')
            self.tree2.heading('#1', text='Alamat')
            self.tree2.heading('#2', text='No Hp')
            self.tree2.heading('#3', text='Jenis')
            self.tree2.heading('#4', text='Harga')
            self.tree2.heading('#5', text='Tanggal Transaksi')
            self.tree2.heading('#6', text='Id Laundry')
            self.tree2.heading('#7', text='Berat Pakaian')
            self.tree2.heading('#8', text='Layanan Antar Jemput')
            self.tree2.heading('#9',text='Diskon')
            self.tree2.heading('#10',text='Total Harga')
            self.tree2.heading('#11', text='Status')

            self.tree2.column('#0',width=100,minwidth=100)
            self.tree2.column('#1',width=100,minwidth=100)
            self.tree2.column('#2',width=100,minwidth=100)
            self.tree2.column('#3',width=100,minwidth=100)
            self.tree2.column('#4',width=100,minwidth=100)
            self.tree2.column('#5',width=100,minwidth=100)
            self.tree2.column('#6',width=100,minwidth=100)
            self.tree2.column('#7',width=100,minwidth=100)
            self.tree2.column('#8',width=100,minwidth=100)
            self.tree2.column('#9',width=100,minwidth=100)
            self.tree2.column('#10',width=100,minwidth=100)
            self.tree2.column('#11',width=100,minwidth=100)
            self.tree2.grid(row=0,columnspan=1,pady=0,sticky='nsew')
         
            self.labelframe4 = tk.LabelFrame(Laundry4,bd=5)
            self.labelframe4.place(x=0,y=535)
            self.labelframe4.grid_propagate(0)
            self.labelframe4.config(width=1210,height=60)

            def insert_data():
                if self.Box_jenis.get()=='Paket Express (1 Hari)':
                    Harga=tk.StringVar()
                    Diskon=tk.StringVar()
                    Total=tk.StringVar()
                    Harga.set(self.Paket_Express)
                    try:
                        berat=int(self.Entry_berat_pakaian.get())
                    except: 
                        showerror(title='Erorr',message='Berat Harus Berupa Angka')
                    if self.Box_antar_jemput.get()=='Yes':
                        jumlah=self.Paket_Express*berat+5000
                        Total.set(jumlah)
                        if jumlah>=100000:
                            diskon=jumlah*15/100
                            Diskon.set(int(diskon))                                
                            total_setelah_diskon=jumlah-diskon
                            Total.set(int(total_setelah_diskon))
                        else:
                            Diskon.set(0)
                    elif self.Box_antar_jemput.get()=='No':
                        jumlah=self.Paket_Express*berat
                        Total.set(jumlah)
                        if jumlah>=100000:
                            diskon=jumlah*15/100
                            Diskon.set(int(diskon))                                
                            total_setelah_diskon=jumlah-diskon
                            Total.set(int(total_setelah_diskon))
                        else:
                            Diskon.set(0)

                elif self.Box_jenis.get()=='Paket Reguler (2 Hari)':
                    Harga=tk.StringVar()
                    Diskon=tk.StringVar()
                    Total=tk.StringVar()
                    Harga.set(self.Paket_Reguler)
                    try:
                        berat=int(self.Entry_berat_pakaian.get())
                    except: 
                        showerror(title='Erorr',message='Berat Harus Berupa Angka')
                    if self.Box_antar_jemput.get()=='Yes':
                        jumlah=self.Paket_Reguler*berat+5000
                        Total.set(jumlah)
                        if jumlah>=100000:
                            diskon=jumlah*15/100
                            Diskon.set(int(diskon))
                            total_setelah_diskon=jumlah-diskon
                            Total.set(int(total_setelah_diskon))
                        else:
                            Diskon.set(0)
                    elif self.Box_antar_jemput.get()=='No':
                        jumlah=self.Paket_Reguler*berat
                        Total.set(jumlah)
                        if jumlah>=100000:
                            diskon=jumlah*15/100
                            Diskon.set(int(diskon))
                            total_setelah_diskon=jumlah-diskon
                            Total.set(int(total_setelah_diskon))
                        else:
                            Diskon.set(0)

                elif self.Box_jenis.get()=='Paket Cuci Kering Express':
                    Harga=tk.StringVar()
                    Diskon=tk.StringVar()
                    Total=tk.StringVar()
                    Harga.set(self.Cuci_Kering_Express)
                    try:
                        berat=int(self.Entry_berat_pakaian.get())
                    except: 
                        showerror(title='Erorr',message='Berat Harus Berupa Angka')
                    if self.Box_antar_jemput.get()=='Yes':
                        jumlah=self.Cuci_Kering_Express*berat+5000
                        Total.set(jumlah)
                        if jumlah>=100000:
                            diskon=jumlah*15/100
                            Diskon.set(int(diskon))
                            total_setelah_diskon=jumlah-diskon
                            Total.set(int(total_setelah_diskon))
                        else:
                            Diskon.set(0)
                    elif self.Box_antar_jemput.get()=='No':
                        jumlah=self.Cuci_Kering_Express*berat
                        Total.set(jumlah)
                        if jumlah>=100000:
                            diskon=jumlah*15/100
                            Diskon.set(int(diskon))
                            total_setelah_diskon=jumlah-diskon
                            Total.set(int(total_setelah_diskon))
                        else:
                            Diskon.set(0)

                elif self.Box_jenis.get()=='Paket Cuci Kering Biasa':
                    Harga=tk.StringVar()
                    Diskon=tk.StringVar()
                    Total=tk.StringVar()
                    Harga.set(self.Cuci_Kering_Biasa)
                    try:
                        berat=int(self.Entry_berat_pakaian.get())
                    except: 
                        showerror(title='Erorr',message='Berat Harus Berupa Angka')
                    if self.Box_antar_jemput.get()=='Yes':
                        jumlah=self.Cuci_Kering_Biasa*berat+5000
                        Total.set(jumlah)
                        if jumlah>=100000:
                            diskon=jumlah*15/100
                            Diskon.set(int(diskon))
                            total_setelah_diskon=jumlah-diskon
                            Total.set(int(total_setelah_diskon))
                        else:
                            Diskon.set(0)
                    elif self.Box_antar_jemput.get()=='No':
                        jumlah=self.Cuci_Kering_Biasa*berat
                        Total.set(jumlah)
                        if jumlah>=100000:
                            diskon=jumlah*15/100
                            Diskon.set(int(diskon))
                            total_setelah_diskon=jumlah-diskon
                            Total.set(int(total_setelah_diskon))
                        else:
                            Diskon.set(0)
                
                elif self.Box_jenis.get()=='Bedcover Express':
                    Harga=tk.StringVar()
                    Diskon=tk.StringVar()
                    Total=tk.StringVar()
                    Harga.set(self.Bedcover_Express)
                    try:
                        berat=int(self.Entry_berat_pakaian.get())
                    except: 
                        showerror(title='Erorr',message='Berat Harus Berupa Angka')
                    if self.Box_antar_jemput.get()=='Yes':
                        jumlah=self.Bedcover_Express*berat+5000
                        Total.set(jumlah)
                        if jumlah>=100000:
                            diskon=jumlah*15/100
                            Diskon.set(int(diskon))
                            total_setelah_diskon=jumlah-diskon
                            Total.set(int(total_setelah_diskon))
                        else:
                            Diskon.set(0)
                    elif self.Box_antar_jemput.get()=='No':
                        jumlah=self.Bedcover_Express*berat
                        Total.set(jumlah)
                        if jumlah>=100000:
                            diskon=jumlah*15/100
                            Diskon.set(int(diskon))
                            total_setelah_diskon=jumlah-diskon
                            Total.set(int(total_setelah_diskon))
                        else:
                            Diskon.set(0)

                elif self.Box_jenis.get()=='Bedcover Biasa':
                    Harga=tk.StringVar()
                    Diskon=tk.StringVar()
                    Total=tk.StringVar()
                    Harga.set(self.Bedcover_Biasa)
                    try:
                        berat=int(self.Entry_berat_pakaian.get())
                    except: 
                        showerror(title='Erorr',message='Berat Harus Berupa Angka')
                    if self.Box_antar_jemput.get()=='Yes':
                        jumlah=self.Bedcover_Biasa*berat+5000
                        Total.set(jumlah)
                        if jumlah>=100000:
                            diskon=jumlah*15/100
                            Diskon.set(int(diskon))
                            total_setelah_diskon=jumlah-diskon
                            Total.set(int(total_setelah_diskon))
                        else:
                            Diskon.set(0)
                    elif self.Box_antar_jemput.get()=='No':
                        jumlah=self.Bedcover_Biasa*berat
                        Total.set(jumlah)
                        if jumlah>=100000:
                            diskon=jumlah*15/100
                            Diskon.set(int(diskon))
                            total_setelah_diskon=jumlah-diskon
                            Total.set(int(total_setelah_diskon))
                        else:
                            Diskon.set(0)
                        
                elif self.Box_jenis.get()=='Helm':
                    Harga=tk.StringVar()
                    Diskon=tk.StringVar()
                    Total=tk.StringVar()
                    Harga.set(self.Helm)
                    try:
                        berat=int(self.Entry_berat_pakaian.get())
                    except: 
                        showerror(title='Erorr',message='Berat Harus Berupa Angka')
                    if self.Box_antar_jemput.get()=='Yes':
                        jumlah=self.Helm*berat+5000
                        Total.set(jumlah)
                        if jumlah>=100000:
                            diskon=jumlah*15/100
                            Diskon.set(int(diskon))
                            total_setelah_diskon=jumlah-diskon
                            Total.set(int(total_setelah_diskon))
                        else:
                            Diskon.set(0)
                    elif self.Box_antar_jemput.get()=='No':
                        jumlah=self.Helm*berat
                        Total.set(jumlah)
                        if jumlah>=100000:
                            diskon=jumlah*15/100
                            Diskon.set(int(diskon))
                            total_setelah_diskon=jumlah-diskon
                            Total.set(int(total_setelah_diskon))
                        else:
                            Diskon.set(0)
                     
                self.tree2.insert('','end',text=(self.Entry_nama.get()),values=(self.Entry_alamat.get(),self.Entry_no_hp.get(),self.Box_jenis.get(),Harga.get(),self.Entry_tgl_transaksi.get(),self.Entry_id_laundry.get(),self.Entry_berat_pakaian.get(),self.Box_antar_jemput.get(),Diskon.get(),Total.get(),self.Box_status.get()))
                
            self.insert_button = tk.Button(self.labelframe4, text = "INSERT",relief='groove',bg='SteelBlue2',fg='white',font='verdana  10 bold ',padx=45,pady=2,command=insert_data)
            self.insert_button.grid(row = 0, column = 0,padx=0,pady=0) 
            self.insert_button.config(height=2,width=23)
            
            def clear_entry():
                self.Box_jenis.current(0)
                self.Box_antar_jemput.current(0)
                self.Box_status.current(0)
                self.Entry_nama.delete(0,tk.END)
                self.Entry_alamat.delete(0,tk.END)
                self.Entry_no_hp.delete(0,tk.END)
                self.Entry_tgl_transaksi.delete(0,tk.END)
                self.Entry_berat_pakaian.delete(0,tk.END)
                self.Entry_id_laundry.delete(0,tk.END)
            self.clear_button=tk.Button(self.labelframe4,text='CLEAR',relief='groove',bg='SteelBlue2',fg='white',font='verdana  10 bold ',command=clear_entry,padx=40,pady=2)
            self.clear_button.grid(row=0,column=2,padx=0,pady=0)
            self.clear_button.config(height=2,width=23)

            def back():
                Menu.Laundry(self)
                Laundry4.destroy()
            self.kembali_button=tk.Button(self.labelframe4,text='BACK',font='verdana  10 bold ',relief='groove',bg='SteelBlue2',fg='white',command=back,padx=50,pady=2)
            self.kembali_button.grid(row=0,column=4,padx=0,pady=0)
            self.kembali_button.config(height=2,width=23)
            

            def remove():
                a=self.tree2.selection()[0]  
                self.tree2.delete(a)
            self.remove_button=tk.Button(self.labelframe4,text='DELETE',relief='groove',bg='SteelBlue2',fg='white',font='verdana  10 bold ',command=remove,padx=40,pady=2)
            self.remove_button.grid(row=0,column=3,padx=0,pady=0)
            self.remove_button.config(height=2,width=23)


class Menu(Login,Jenis,Transaksi):
    def __init__(self):
        self.Teks1=None
        self.Tombol_jenis_laundry=None
        self.Tombol_transaksi=None
        self.Tombol_logout=None
        Login.__init__(self)

    def Laundry(self):
        Laundry2=tk.Toplevel()
        Laundry2.geometry('500x300')
        Laundry2.title('Menu Laundry')
        Laundry2.configure(bg='pink')

        def Go_To_Jenis():
            Jenis.Laundry(self)
            Laundry2.destroy()
        self.Teks1=tk.Label(Laundry2,text="...LAUNDRY...",background='pink',font='Heltevica  35 bold italic')
        self.Teks1.place(x=100,y=0) 
         
        self.Tombol_jenis_laundry=tk.Button(Laundry2, text="Jenis Laundry",relief='raised',width=20,font='verdana  12 bold ',background='SteelBlue2',activebackground='green2',fg='white',command=Go_To_Jenis)
        self.Tombol_jenis_laundry.place(x=140,y=80)

        def Go_To_Transaksi():
            Transaksi.__init__(self)
            Laundry2.destroy()
        self.Tombol_transaksi=tk.Button(Laundry2, text="Transaksi",width=20,relief='raised',font='verdana  12 bold',background='SteelBlue2',activebackground='green2',fg='white',command=Go_To_Transaksi)
        self.Tombol_transaksi.place(x=140,y=150)

        def Exit():
            showinfo(title="Thank You", message="You log out")
            exit()
        self.Tombol_logout=tk.Button(Laundry2, text="LOG OUT",font='verdana  12 bold',relief='raised',width=20,background='SteelBlue2',activebackground='red2',fg='white',command=Exit)
        self.Tombol_logout.place(x=140,y=220) 

# L=Login()
M=Menu()
# M.__init__()
Laundry.mainloop()




