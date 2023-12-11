from tkinter.messagebox import showinfo
import tkinter as tk
import sqlite3
from tkinter.ttk import Combobox,Treeview



Laundry=tk.Tk()
#Laundry.config(bg='silver')

from abc import ABC,abstractmethod
class laundry(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def Laundry(self):
        pass

    @abstractmethod
    def Button(self):
        pass
    
class Jenis():
    def __init__(self):
        self.Teks3=None
        self.tree=None
        self.Frame=None
        self.Teks_note=None
        self.kembali=None
        self.Tombol_jenis_laundry=None
              
    def Laundry(self):
            # self.Tombol_transaksi.destroy(),self.Tombol_logout.destroy(),
            self.Tombol_jenis_laundry.destroy()
    
            # self.Teks2=tk.Label(Laundry,text="...LAUNDRY...",font='Heltevica  35 bold italic')
            # self.Teks2.place(x=200,y=0)

            self.Teks3=tk.Label(Laundry,text="..Jenis Laundry..",font='Arial  15  italic')
            self.Teks3.place(x=270,y=50)

            self.tree=Treeview(Laundry,columns=('#0','#1'))
            self.tree.heading('#0', text='No')
            self.tree.heading('#1', text='Jenis Layanan')
            self.tree.heading('#2', text='Harga')

            self.tree.column('#0',width=10,minwidth=50)
            self.tree.column('#1',minwidth=100)
            self.tree.grid(row=0,columnspan=1,pady=120,padx=150,sticky='nsew')
            self.tree.config(height=7)

            self.tree.insert('','end',text='1',values=('Paket Express (1 Hari)','Rp. 12.000/Kg'))
            self.tree.insert('','end',text='2',values=('Paket Reguler (2 Hari)','Rp. 8.000/Kg'))
            self.tree.insert('','end',text='3',values=('Paket Cuci Kering Express','Rp. 7.000/Kg'))
            self.tree.insert('','end',text='4',values=('Paket Cuci Kering Biasa','Rp. 5.000/Kg'))
            self.tree.insert('','end',text='5',values=('Bedcover Express','Rp. 30.000/pcs'))
            self.tree.insert('','end',text='6',values=('Bedcover Biasa','Rp. 20.000/pcs'))
            self.tree.insert('','end',text='7',values=('Helm','Rp. 25.000/pcs'))

            self.Frame = tk.LabelFrame(Laundry,bd=5)
            self.Frame.place(x=150,y=288)
           
            self.Teks_note=tk.Label(self.Frame,text='''NOTE:
            Jika anda memilih layanan antar jemput maka tambah biaya Rp 5.000
            Jika jumlah lebih dari 100.000 rb maka mendapatkan diskon 15%''')
            self.Teks_note.grid()

            def back():
                self.tree.destroy(),self.Teks3.destroy(),self.kembali.destroy(),self.Frame.destroy()
                self.Button()
            self.kembali=tk.Button(Laundry,text='Back',command=back,width=10,font='verdana  8 bold ',background='silver',fg='black')
            self.kembali.place(x=470,y=370)

    def Button(self):
        self.Tombol_jenis_laundry=tk.Button(Laundry, text="Jenis Laundry",width=20,font='verdana  12 bold ',background='white',fg='black',command=self.Laundry)
        self.Tombol_jenis_laundry.place(x=240,y=100)

class Transaksi(laundry,Jenis):
    def __init__(self):
        Jenis.__init__(self)
        self.Teks5=None
        self.Teks6=None
        self.labelframe1=None
        self.labelframe2=None
        self.Teks_nama=None
        self.Entry_nama=None
        self.Teks_alamat=None
        self.Entry_alamat=None
        self.__Teks_no_hp=None
        self.__Entry_no_hp=None
        self.Teks_jenis=None
        self.Pilihan_jenis=None
        self.Box_jenis=None
        self.Teks_Harga=None
        self.Entry_Harga=None
        self.Teks_tgl_transaksi=None
        self.Entry_tgl_transaksi=None
        self.Teks_id_laundry=None
        self.Entry_id_laundry=None
        self.Teks_berat_pakaian=None
        self.Entry_berat_pakaian=None
        self.Teks_layanan_antar_jemput=None
        self.Pilihan_antar_jemput=None
        self.Box_antar_jemput=None
        self.Teks_status=None
        self.Pilihan_status=None
        self.Box_status=None
        self.labelframe3=None
        self.tree2=None
        self.labelframe4=None
        self.insert_button=None
        self.clear_button=None
        self.kembali_button=None
        self.remove_button=None
        self.Tombol_logout=None
        Jenis.__init__(self)

        
    def Laundry(self):
            a=Laundry.geometry('1200x600')

            self.Tombol_transaksi.destroy(),self.Teks4.destroy(),self.Tombol_logout.destroy()
            #self.Tombol_jenis_laundry.destroy(),
            # self.Teks2.destroy()

            self.Teks5=tk.Label(Laundry,text="...LAUNDRY...",font='Heltevica  35 bold italic')
            self.Teks5.place(x=450,y=0)

            self.Teks6=tk.Label(Laundry,text="Transaksi Laundry",font='Courier  15 bold')
            self.Teks6.place(x=500,y=60)

            self.labelframe1 = tk.LabelFrame(Laundry, text="Data Transaksi",bd=5)#bg='silver')
            self.labelframe1.place(x=0,y=85)
            self.labelframe1.grid_propagate(0)
            self.labelframe1.config(width=620,height=300)

            self.labelframe2 = tk.LabelFrame(Laundry,bd=5)
            self.labelframe2.place(x=615,y=90)
            self.labelframe2.grid_propagate(0)
            self.labelframe2.config(width=590,height=300)

            self.Teks_nama=tk.Label(self.labelframe1,text="NAMA",padx=5,pady=0)
            self.Teks_nama.grid(column=1,row=0,sticky='W')
            self.Entry_nama=tk.Entry(self.labelframe1,width=30)
            self.Entry_nama.grid(column=50,row=0,padx=50,pady=0)

            self.Teks_alamat=tk.Label(self.labelframe1,text="ALAMAT",padx=5,pady=0)
            self.Teks_alamat.grid(column=1,row=2,sticky='W')
            self.Entry_alamat=tk.Entry(self.labelframe1,width=30)
            self.Entry_alamat.grid(column=50,row=2,padx=153,pady=0)
    
            self.__Teks_no_hp=tk.Label(self.labelframe1,text="NO HP",padx=5,pady=0)
            self.__Teks_no_hp.grid(column=1,row=3,sticky='W')
            self.__Entry_no_hp=tk.Entry(self.labelframe1,width=30)
            self.__Entry_no_hp.grid(column=50,row=3,padx=153,pady=0)
              
            self.Teks_jenis=tk.Label(self.labelframe1,text="JENIS LAUNDRY",padx=5,pady=0)
            self.Teks_jenis.grid(column=1,row=4,sticky='W')
            
            self.Pilihan_jenis=['Pilih Jenis','Paket Express (1 Hari)','Paket Reguler (2 Hari)','Paket Cuci Kering Express','Paket Cuci Kering Biasa','Bedcover Express','Bedcover Biasa','Helm']
            self.Box_jenis=Combobox(self.labelframe1,values=self.Pilihan_jenis,width=27)
            self.Box_jenis.grid(column=50,row=4,padx=95,pady=0)
            self.Box_jenis.current(0)

            self.Teks_Harga=tk.Label(self.labelframe1,text="HARGA",padx=5,pady=0)
            self.Teks_Harga.grid(column=1,row=5,sticky='W')
            self.Entry_Harga=tk.Entry(self.labelframe1,width=30)
            self.Entry_Harga.grid(column=50,row=5,padx=95,pady=0)

            self.Teks_tgl_transaksi=tk.Label(self.labelframe1,text="TANGGAL TRANSAKSI",padx=5,pady=0)
            self.Teks_tgl_transaksi.grid(column=1,row=6,sticky='W')
            self.Entry_tgl_transaksi=tk.Entry(self.labelframe1,width=30)
            self.Entry_tgl_transaksi.grid(column=50,row=6,padx=95,pady=0)

            self.Teks_id_laundry=tk.Label(self.labelframe1,text="ID LAUNDRY",padx=5,pady=0)
            self.Teks_id_laundry.grid(column=1,row=7,sticky='W')
            self.Entry_id_laundry=tk.Entry(self.labelframe1,width=30)
            self.Entry_id_laundry.grid(column=50,row=7,padx=95,pady=0)

            self.Teks_berat_pakaian=tk.Label(self.labelframe1,text="BERAT PAKAIAN",padx=5,pady=0)
            self.Teks_berat_pakaian.grid(column=1,row=8,sticky='W')
            self.Entry_berat_pakaian=tk.Entry(self.labelframe1,width=30)
            self.Entry_berat_pakaian.grid(column=50,row=8,padx=95,pady=0)

            self.Teks_layanan_antar_jemput=tk.Label(self.labelframe1,text="LAYANAN ANTAR JEMPUT",padx=5,pady=0)
            self.Teks_layanan_antar_jemput.grid(column=1,row=9,sticky='W')
            
            self.Pilihan_antar_jemput=['Pilih Layanan','No','Yes',]
            self.Box_antar_jemput=Combobox(self.labelframe1,values=self.Pilihan_antar_jemput,width=27)
            self.Box_antar_jemput.grid(column=50,row=9,padx=95,pady=0)
            self.Box_antar_jemput.current(0)

            self.Teks_status=tk.Label(self.labelframe1,text="STATUS",padx=5,pady=0)
            self.Teks_status.grid(column=1,row=10,sticky='W')
            self.Pilihan_status=['Pilih Status','Lunas','Belum Bayar']
            self.Box_status=Combobox(self.labelframe1,values=self.Pilihan_status,width=27)
            self.Box_status.grid(column=50,row=10,padx=95,pady=0)
            self.Box_status.current(0)
           
            self.labelframe3 = tk.LabelFrame(Laundry,bd=5)
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
         
            self.labelframe4 = tk.LabelFrame(Laundry,bd=5)
            self.labelframe4.place(x=0,y=535)
            self.labelframe4.grid_propagate(0)
            self.labelframe4.config(width=1210,height=60)

            def insert_data():
                if self.Box_antar_jemput.get()=='Yes':
                    Total=tk.StringVar()
                    Diskon=tk.StringVar()
                    try : 
                        harga=int(self.Entry_Harga.get())
                        berat=int(self.Entry_berat_pakaian.get())
                        jumlah=harga*berat+5000
                        Total.set(jumlah)
                        if jumlah>=100000:
                            diskon=jumlah*15/100
                            Diskon.set(int(diskon))
                            total_setelah_diskon=jumlah-diskon
                            Total.set(int(total_setelah_diskon))
                    except :
                        print('===HARGA DAN BERAT HARUS BERUPA ANGKA===')
                    
                elif self.Box_antar_jemput.get()=='No':
                    Total=tk.StringVar()
                    Diskon=tk.StringVar()
                    try : 
                        harga=int(self.Entry_Harga.get())
                        berat=int(self.Entry_berat_pakaian.get())
                        jumlah=harga*berat
                        Total.set(jumlah)
                        if jumlah>=100000:
                            diskon=jumlah*15/100
                            Diskon.set(int(diskon))
                            total_setelah_diskon=jumlah-diskon
                            Total.set(int(total_setelah_diskon))
                    except :
                        print('===HARGA DAN BERAT HARUS BERUPA ANGKA===')

                self.tree2.insert('','end',text=(self.Entry_nama.get()),values=(self.Entry_alamat.get(),self.__Entry_no_hp.get(),self.Box_jenis.get(),self.Entry_Harga.get(),self.Entry_tgl_transaksi.get(),self.Entry_id_laundry.get(),self.Entry_berat_pakaian.get(),self.Box_antar_jemput.get(),Diskon.get(),Total.get(),self.Box_status.get()))
            self.insert_button = tk.Button(self.labelframe4, text = "INSERT",font='verdana  10 bold ',padx=45,pady=2,bg='silver',command=insert_data)
            self.insert_button.grid(row = 0, column = 0,padx=0,pady=0) 
            self.insert_button.config(height=2,width=23)
            

            def clear_entry():
                self.Box_jenis.current(0)
                self.Box_antar_jemput.current(0)
                self.Box_status.current(0)
                self.Entry_nama.delete(0,tk.END)
                self.Entry_alamat.delete(0,tk.END)
                self.__Entry_no_hp.delete(0,tk.END)
                self.Entry_Harga.delete(0,tk.END)
                self.Entry_tgl_transaksi.delete(0,tk.END)
                self.Entry_berat_pakaian.delete(0,tk.END)
                self.Entry_id_laundry.delete(0,tk.END)
            self.clear_button=tk.Button(self.labelframe4,text='CLEAR',font='verdana  10 bold ',command=clear_entry,padx=40,pady=2,background='silver')
            self.clear_button.grid(row=0,column=2,padx=0,pady=0)
            self.clear_button.config(height=2,width=23)

            def back():
                self.labelframe1.destroy(),self.Teks5.destroy(),self.Teks6.destroy(),self.tree2.destroy(),self.labelframe2.destroy(),self.labelframe1.destroy(),self.labelframe3.destroy(),self.labelframe4.destroy()
                self.Button()
            self.kembali_button=tk.Button(self.labelframe4,text='BACK',font='verdana  10 bold ',command=back,padx=50,pady=2,background='silver')
            self.kembali_button.grid(row=0,column=4,padx=0,pady=0)
            self.kembali_button.config(height=2,width=23)
            

            def remove():
                a=self.tree2.selection()[0]  
                self.tree2.delete(a)
            self.remove_button=tk.Button(self.labelframe4,text='DELETE',font='verdana  10 bold ',command=remove,padx=40,pady=2,background='silver')
            self.remove_button.grid(row=0,column=3,padx=0,pady=0)
            self.remove_button.config(height=2,width=23)

    def Button(self):
        Laundry.geometry('700x400')
        self.Teks4=tk.Label(Laundry,text="...LAUNDRY...",font='Heltevica  35 bold italic')
        self.Teks4.place(x=200,y=0) 
        self.Tombol_transaksi=tk.Button(Laundry, text="Transaksi",width=20,font='verdana  12 bold',background='white',fg='black',command=self.Laundry)
        self.Tombol_transaksi.place(x=240,y=180)
        def Exit():
            showinfo(title="Thank You", message="You log out")
            exit()
        self.Tombol_logout=tk.Button(Laundry, text="LOG OUT",font='verdana  12 bold ',width=20,background='white',fg='black',command=Exit)
        self.Tombol_logout.place(x=240,y=260) 

Laundry.title('Laundry')
T=Transaksi()
J=Jenis()
T.Button()
J.Button()
Laundry.mainloop()

# class Menu(laundry,Jenis,Transaksi):
#     def __init__(self):
#         self.Teks1=None
#         self.Tombol_jenis_laundry=None
#         self.Tombol_transaksi=None
#         self.Tombol_logout=None

    # def Laundry(self):
    #     Laundry.geometry('700x400')
    #     self.Teks1=tk.Label(Laundry,text="...LAUNDRY...",font='Heltevica  35 bold italic')
    #     self.Teks1.place(x=200,y=0) 
         
        
    #     #self.a=Jenis.Laundry()
    #     # self.Tombol_jenis_laundry=tk.Button(Laundry, text="Jenis Laundry",width=20,font='verdana  12 bold ',background='white',fg='black',command=self.Laundry)
    #     # self.Tombol_jenis_laundry.place(x=240,y=100)

    #     # self.Tombol_transaksi=tk.Button(Laundry, text="Transaksi",width=20,font='verdana  12 bold',background='white',fg='black',command=self.Laundry)
    #     # self.Tombol_transaksi.place(x=240,y=180)

    #     def Exit():
    #         showinfo(title="Thank You", message="You log out")
    #         exit()
    #     self.Tombol_logout=tk.Button(Laundry, text="LOG OUT",font='verdana  12 bold ',width=20,background='white',fg='black',command=Exit)
    #     self.Tombol_logout.place(x=240,y=260) 

# Laundry.title('Laundry')
# T=Transaksi()
# J=Jenis()
# J.Button()
# T.Button()
# Laundry.mainloop()


        # def jenis_laundry():
        #     self.Tombol_transaksi.destroy(),self.Tombol_logout.destroy(),self.Tombol_jenis_laundry.destroy()
        #     Teks1.destroy()
    
        #     Teks2=tk.Label(Laundry,text="...LAUNDRY...",font='Heltevica  35 bold italic')
        #     Teks2.place(x=200,y=0)

        #     Teks3=tk.Label(Laundry,text="..Jenis Laundry..",font='Arial  15  italic')
        #     Teks3.place(x=270,y=50)

        #     tree=Treeview(Laundry,columns=('#0','#1'))
        #     tree.heading('#0', text='No')
        #     tree.heading('#1', text='Jenis Layanan')
        #     tree.heading('#2', text='Harga')

        #     tree.column('#0',width=10,minwidth=50)
        #     tree.column('#1',minwidth=100)
        #     tree.grid(row=0,columnspan=1,pady=120,padx=150,sticky='nsew')
        #     tree.config(height=7)

        #     tree.insert('','end',text='1',values=('Paket Express (1 Hari)','Rp. 12.000/Kg'))
        #     tree.insert('','end',text='2',values=('Paket Reguler (2 Hari)','Rp. 8.000/Kg'))
        #     tree.insert('','end',text='3',values=('Paket Cuci Kering Express','Rp. 7.000/Kg'))
        #     tree.insert('','end',text='4',values=('Paket Cuci Kering Biasa','Rp. 5.000/Kg'))
        #     tree.insert('','end',text='5',values=('Bedcover Express','Rp. 30.000/pcs'))
        #     tree.insert('','end',text='6',values=('Bedcover Biasa','Rp. 20.000/pcs'))
        #     tree.insert('','end',text='7',values=('Helm','Rp. 25.000/pcs'))

        #     Frame = tk.LabelFrame(Laundry,bd=5)
        #     Frame.place(x=150,y=288)
           
        #     Teks_note=tk.Label(Frame,text='''NOT:
        #     Jika anda memilih layanan antar jemput maka tambah biaya Rp 5.000
        #     Jika jumlah lebih dari 100.000 rb maka mendapatkan diskon 15%''')
        #     Teks_note.grid()

        #     def back():
        #         tree.destroy(),Teks2.destroy(),Teks3.destroy(),kembali.destroy(),Frame.destroy()
        #         self.Menu()
        #     kembali=tk.Button(Laundry,text='Back',command=back,width=10,font='verdana  8 bold ',background='silver',fg='black')
        #     kembali.place(x=470,y=370)

        # def Transaksi():
        #     a=Laundry.geometry('1200x600')

        #     self.Tombol_transaksi.destroy(),self.Tombol_logout.destroy(),self.Tombol_jenis_laundry.destroy()
        #     self.Teks1.destroy()

        #     Teks2=tk.Label(Laundry,text="...LAUNDRY...",font='Heltevica  35 bold italic')
        #     Teks2.place(x=450,y=0)

        #     Teks3=tk.Label(Laundry,text="Transaksi Laundry",font='Courier  15 bold')
        #     Teks3.place(x=500,y=60)

        #     labelframe1 = tk.LabelFrame(Laundry, text="Data Transaksi",bd=5)#bg='silver')
        #     labelframe1.place(x=0,y=85)
        #     labelframe1.grid_propagate(100)
        #     labelframe1.config(width=620,height=300)

        #     labelframe2 = tk.LabelFrame(Laundry,bd=5)
        #     labelframe2.place(x=615,y=90)
        #     labelframe2.grid_propagate(0)
        #     labelframe2.config(width=590,height=300)

        #     Teks_nama=tk.Label(labelframe1,text="NAMA",padx=5,pady=0)
        #     Teks_nama.grid(column=1,row=0,sticky='W')
        #     Entry_nama=tk.Entry(labelframe1,width=30)
        #     Entry_nama.grid(column=50,row=0,padx=50,pady=0)

        #     Teks_alamat=tk.Label(labelframe1,text="ALAMAT",padx=5,pady=0)
        #     Teks_alamat.grid(column=1,row=2,sticky='W')
        #     Entry_alamat=tk.Entry(labelframe1,width=30)
        #     Entry_alamat.grid(column=50,row=2,padx=153,pady=0)

        #     Teks_no_hp=tk.Label(labelframe1,text="NO HP",padx=5,pady=0)
        #     Teks_no_hp.grid(column=1,row=3,sticky='W')
        #     Entry_no_hp=tk.Entry(labelframe1,width=30)
        #     Entry_no_hp.grid(column=50,row=3,padx=153,pady=0)
              
        #     Teks_jenis=tk.Label(labelframe1,text="JENIS LAUNDRY",padx=5,pady=0)
        #     Teks_jenis.grid(column=1,row=4,sticky='W')
            
        #     Pilihan_jenis=['Pilih Jenis','Paket Express (1 Hari)','Paket Reguler (2 Hari)','Paket Cuci Kering Express','Paket Cuci Kering Biasa','Bedcover Express','Bedcover Biasa','Helm']
        #     Box_jenis=Combobox(labelframe1,values=Pilihan_jenis,width=27)
        #     Box_jenis.grid(column=50,row=4,padx=95,pady=0)
        #     Box_jenis.current(0)

        #     Teks_Harga=tk.Label(labelframe1,text="HARGA",padx=5,pady=0)
        #     Teks_Harga.grid(column=1,row=5,sticky='W')
        #     Entry_Harga=tk.Entry(labelframe1,width=30)
        #     Entry_Harga.grid(column=50,row=5,padx=95,pady=0)

        #     Teks_tgl_transaksi=tk.Label(labelframe1,text="TANGGAL TRANSAKSI",padx=5,pady=0)
        #     Teks_tgl_transaksi.grid(column=1,row=6,sticky='W')
        #     Entry_tgl_transaksi=tk.Entry(labelframe1,width=30)
        #     Entry_tgl_transaksi.grid(column=50,row=6,padx=95,pady=0)

        #     Teks_id_laundry=tk.Label(labelframe1,text="ID LAUNDRY",padx=5,pady=0)
        #     Teks_id_laundry.grid(column=1,row=7,sticky='W')
        #     Entry_id_laundry=tk.Entry(labelframe1,width=30)
        #     Entry_id_laundry.grid(column=50,row=7,padx=95,pady=0)

        #     Teks_berat_pakaian=tk.Label(labelframe1,text="BERAT PAKAIAN",padx=5,pady=0)
        #     Teks_berat_pakaian.grid(column=1,row=8,sticky='W')
        #     Entry_berat_pakaian=tk.Entry(labelframe1,width=30)
        #     Entry_berat_pakaian.grid(column=50,row=8,padx=95,pady=0)

        #     Teks_layanan_antar_jemput=tk.Label(labelframe1,text="LAYANAN ANTAR JEMPUT",padx=5,pady=0)
        #     Teks_layanan_antar_jemput.grid(column=1,row=9,sticky='W')
            
        #     Pilihan_antar_jemput=['Pilih Layanan','No','Yes',]
        #     Box_antar_jemput=Combobox(labelframe1,values=Pilihan_antar_jemput,width=27)
        #     Box_antar_jemput.grid(column=50,row=9,padx=95,pady=0)
        #     Box_antar_jemput.current(0)

        #     Teks_status=tk.Label(labelframe1,text="STATUS",padx=5,pady=0)
        #     Teks_status.grid(column=1,row=10,sticky='W')
        #     Pilihan_status=['Pilih Status','Lunas','Belum Bayar']
        #     Box_status=Combobox(labelframe1,values=Pilihan_status,width=27)
        #     Box_status.grid(column=50,row=10,padx=95,pady=0)
        #     Box_status.current(0)
           
        #     Frame = tk.LabelFrame(Laundry,bd=5)
        #     Frame.place(y=300)
        #     Frame.config(height=1)

        #     tree=Treeview(Frame,columns=('#0','#1','#2','#3','#4','#5','#6','#7','#9','#10','#11'))
        #     tree.heading('#0', text='Nama')
        #     tree.heading('#1', text='Alamat')
        #     tree.heading('#2', text='No Hp')
        #     tree.heading('#3', text='Jenis')
        #     tree.heading('#4', text='Harga')
        #     tree.heading('#5', text='Tanggal Transaksi')
        #     tree.heading('#6', text='Id Laundry')
        #     tree.heading('#7', text='Berat Pakaian')
        #     tree.heading('#8', text='Layanan Antar Jemput')
        #     tree.heading('#9',text='Diskon')
        #     tree.heading('#10',text='Total Harga')
        #     tree.heading('#11', text='Status')

        #     tree.column('#0',width=100,minwidth=100)
        #     tree.column('#1',width=100,minwidth=100)
        #     tree.column('#2',width=100,minwidth=100)
        #     tree.column('#3',width=100,minwidth=100)
        #     tree.column('#4',width=100,minwidth=100)
        #     tree.column('#5',width=100,minwidth=100)
        #     tree.column('#6',width=100,minwidth=100)
        #     tree.column('#7',width=100,minwidth=100)
        #     tree.column('#8',width=100,minwidth=100)
        #     tree.column('#9',width=100,minwidth=100)
        #     tree.column('#10',width=100,minwidth=100)
        #     tree.column('#11',width=100,minwidth=100)
        #     tree.grid(row=0,columnspan=1,pady=0,sticky='nsew')
         
        #     labelframe3 = tk.LabelFrame(Laundry,bd=5)
        #     labelframe3.place(x=0,y=535)
        #     labelframe3.grid_propagate(0)
        #     labelframe3.config(width=1210,height=60)

        #     def insert_data():
        #         if Box_antar_jemput.get()=='Yes':
        #             Total=tk.StringVar()
        #             Diskon=tk.StringVar()
        #             harga=int(Entry_Harga.get())
        #             berat=int(Entry_berat_pakaian.get())
        #             jumlah=harga*berat+5000
        #             Total.set(jumlah)
        #             if jumlah>=100000:
        #                 diskon=jumlah*15/100
        #                 Diskon.set(int(diskon))
        #                 total_setelah_diskon=jumlah-diskon
        #                 Total.set(int(total_setelah_diskon))
                    
        #         elif Box_antar_jemput.get()=='No':
        #             Total=tk.StringVar()
        #             Diskon=tk.StringVar()
        #             harga=int(Entry_Harga.get())
        #             berat=int(Entry_berat_pakaian.get())
        #             jumlah=harga*berat
        #             Total.set(jumlah)
        #             if jumlah>=100000:
        #                 diskon=jumlah*15/100
        #                 Diskon.set(int(diskon))
        #                 total_setelah_diskon=jumlah-diskon
        #                 Total.set(int(total_setelah_diskon))

        #         tree.insert('','end',text=(Entry_nama.get()),values=(Entry_alamat.get(),Entry_no_hp.get(),Box_jenis.get(),Entry_Harga.get(),Entry_tgl_transaksi.get(),Entry_id_laundry.get(),Entry_berat_pakaian.get(),Box_antar_jemput.get(),Diskon.get(),Total.get(),Box_status.get()))
        #         Box_jenis.current(0)
        #         Box_antar_jemput.current(0)
        #         Box_status.current(0)
        #         Entry_nama.delete(0,tk.END)
        #         Entry_alamat.delete(0,tk.END)
        #         Entry_no_hp.delete(0,tk.END)
        #         Entry_Harga.delete(0,tk.END)
        #         Entry_tgl_transaksi.delete(0,tk.END)
        #         Entry_berat_pakaian.delete(0,tk.END)
        #         Entry_id_laundry.delete(0,tk.END)
        #     insert_button = tk.Button(labelframe3, text = "INSERT",font='verdana  10 bold ',padx=45,pady=2,bg='silver',command=insert_data)
        #     insert_button.grid(row = 0, column = 0,padx=0,pady=0) 
        #     insert_button.config(height=2,width=23)
            

        #     def clear_entry():
        #         Box_jenis.current(0)
        #         Box_antar_jemput.current(0)
        #         Box_status.current(0)
        #         Entry_nama.delete(0,tk.END)
        #         Entry_alamat.delete(0,tk.END)
        #         Entry_no_hp.delete(0,tk.END)
        #         Entry_Harga.delete(0,tk.END)
        #         Entry_tgl_transaksi.delete(0,tk.END)
        #         Entry_berat_pakaian.delete(0,tk.END)
        #         Entry_id_laundry.delete(0,tk.END)
        #     clear_button=tk.Button(labelframe3,text='CLEAR',font='verdana  10 bold ',command=clear_entry,padx=40,pady=2,background='silver')
        #     clear_button.grid(row=0,column=2,padx=0,pady=0)
        #     clear_button.config(height=2,width=23)


        #     def back():
        #         labelframe1.destroy(),Teks2.destroy(),Teks3.destroy(),tree.destroy(),labelframe2.destroy(),Frame.destroy(),labelframe3.destroy()
        #         self.Menu()
        #     kembali_button=tk.Button(labelframe3,text='BACK',font='verdana  10 bold ',command=back,padx=50,pady=2,background='silver')
        #     kembali_button.grid(row=0,column=4,padx=0,pady=0)
        #     kembali_button.config(height=2,width=23)
            

        #     def remove():
        #         a=tree.selection()[0]  
        #         tree.delete(a)
        #     remove_button=tk.Button(labelframe3,text='DELETE',font='verdana  10 bold ',command=remove,padx=40,pady=2,background='silver')
        #     remove_button.grid(row=0,column=3,padx=0,pady=0)
        #     remove_button.config(height=2,width=23)
            
        # self.Teks1=tk.Label(Laundry,text="...LAUNDRY...",font='Heltevica  35 bold italic')
        # self.Teks1.place(x=200,y=0)
        
        # self.Tombol_jenis_laundry=tk.Button(Laundry, text="Jenis Laundry",width=20,font='verdana  12 bold ',background='white',fg='black',command=self.jenis_laundry)#.pack()
        # self.Tombol_jenis_laundry.place(x=240,y=100)

        # self.Tombol_transaksi=tk.Button(Laundry, text="Transaksi",width=20,font='verdana  12 bold',background='white',fg='black',command=Transaksi)
        # self.Tombol_transaksi.place(x=240,y=180)

        # self.Tombol_logout=tk.Button(Laundry, text="LOG OUT",font='verdana  12 bold ',width=20,background='white',fg='black',command=self.Exit)
        # self.Tombol_logout.place(x=240,y=260)   
    
        

# Laundry.title('Laundry')
# j=jenis()
# Laundry.mainloop()


#font_teks= Font(family='Heltevica',size=10,weight='bold',slant='roman')
# Teks1=tk.Label(Laundry,text="...LAUNDRY...",font='Heltevica  16 bold italic')
# Teks1.pack()
#Teks1.grid(row=0,column=10)

