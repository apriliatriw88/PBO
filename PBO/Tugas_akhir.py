from pickle import NONE
from re import X
from textwrap import fill
from tkinter.messagebox import NO, YES, showinfo
import tkinter as tk
from tkinter.ttk import LabelFrame, Labelframe, Treeview
from tkinter import BOTH, BOTTOM, END, HORIZONTAL, LEFT, RIGHT, Y, Frame, Scrollbar, ttk
from turtle import width
from typing import Text
from functools import partial

Laundry=tk.Tk()
#Laundry.config(bg='silver')

from abc import ABC,abstractmethod

class Laundry1(ABC):
    @abstractmethod
    def __init__(self):
        pass
    @abstractmethod
    def Input_Data(self):
        pass
    @abstractmethod
    def Tampil_Data(self):
        pass

class jenis:
    def __init__(self):#,Tombol_jenis_laundry,Teks1,kembali,Teks2,Teks3):
        self.Tombol_jenis_laundry=None
        self.Teks1=None
        self.kembali=None
        self.Teks2=None
        self.Teks3=None
        self.Tombol_logout=None
        self.Menu()

    def Exit(self):
        showinfo(title="Thank You", message="You log out")
        exit()

    def Menu(self):
        def in_jenis_laundry():
            self.Tombol_transaksi.destroy(),self.Tombol_logout.destroy(),self.Tombol_jenis_laundry.destroy(),self.Tombol_data_pelanggan.destroy()
            Teks1.destroy()

            Teks2=tk.Label(Laundry,text="...LAUNDRY...",font='Heltevica  35 bold italic')
            Teks2.place(x=200,y=60)

            Teks3=tk.Label(Laundry,text="..Jenis Laundry..",font='Arial  15  italic')
            Teks3.place(x=270,y=120)

            a1=tk.Label(Laundry, text='Kode',font='arial  13 bold ')
            a1.place(x=190,y=180)
            a2=tk.Label(Laundry, text="1",font='arial  10 bold ')
            a2.place(x=200,y=210)
            a3=tk.Label(Laundry, text="2",font='arial  10 bold ')
            a3.place(x=200,y=230)
            a4=tk.Label(Laundry, text="3",font='arial  10 bold ')
            a4.place(x=200,y=250)
            a5=tk.Label(Laundry, text="4",font='arial  10 bold ')
            a5.place(x=200,y=270)
            a6=tk.Label(Laundry, text="5",font='arial  10 bold ')
            a6.place(x=200,y=290)
            a7=tk.Label(Laundry, text="6",font='arial  10 bold ')
            a7.place(x=200,y=310)
            a8=tk.Label(Laundry, text="7",font='arial  10 bold ')
            a8.place(x=200,y=330)
            a9=tk.Label(Laundry, text="Jenis Layanan",font='arial  13 bold')
            a9.place(x=280,y=180)
            a10=tk.Label(Laundry, text="Paket Express (1 Hari)",font='arial  10 bold ')
            a10.place(x=270,y=210)
            a11=tk.Label(Laundry, text="Paket Reguler (2 Hari)",font='arial  10 bold ')
            a11.place(x=270,y=230)
            a12=tk.Label(Laundry, text="Paket Cuci Kering Express",font='arial  10 bold ')
            a12.place(x=260,y=250)
            a13=tk.Label(Laundry, text="Paket Cuci Kering Biasa",font='arial  10 bold ')
            a13.place(x=265,y=270)
            a14=tk.Label(Laundry, text="Bedcover Express",font='arial  10 bold ')
            a14.place(x=285,y=290)
            a15=tk.Label(Laundry, text="Bedcover Biasa",font='arial  10 bold ')
            a15.place(x=290,y=310)
            a16=tk.Label(Laundry, text="Helm",font='arial  10 bold ')
            a16.place(x=320,y=330)
            a17=tk.Label(Laundry, text="Harga",font='arial  13 bold ')
            a17.place(x=470,y=180)
            a18=tk.Label(Laundry, text="Rp. 12.000/Kg",font='arial  10 bold ')
            a18.place(x=450,y=210)
            a19=tk.Label(Laundry, text="Rp. 8.000/Kg",font='arial  10 bold ')
            a19.place(x=450,y=230)
            a20=tk.Label(Laundry, text="Rp. 7.000/Kg",font='arial  10 bold ')
            a20.place(x=450,y=250)
            a21=tk.Label(Laundry, text="Rp. 5.000/Kg",font='arial  10 bold ')
            a21.place(x=450,y=270)
            a22=tk.Label(Laundry, text="Rp. 30.000/Pcs",font='arial  10 bold ')
            a22.place(x=450,y=290)
            a23=tk.Label(Laundry, text="Rp. 20.000/Pcs",font='arial  10 bold ')
            a23.place(x=450,y=310)
            a24=tk.Label(Laundry, text="Rp. 25.000/Pcs",font='arial  10 bold ')
            a24.place(x=450,y=330)

            def back():
                a1.destroy(),a2.destroy(),a3.destroy(),a4.destroy(),a5.destroy(),a6.destroy(),a7.destroy(),a8.destroy(),a9.destroy(),a10.destroy(),a11.destroy(),a12.destroy(),a13.destroy(),a14.destroy(),a15.destroy(),a16.destroy(),a17.destroy(),a18.destroy(),a19.destroy(),a20.destroy(),a21.destroy(),a22.destroy(),a23.destroy(),a24.destroy()
                Teks2.destroy(),Teks3.destroy()
                kembali.destroy()
                self.Menu()
            kembali=tk.Button(Laundry,text='Back',command=back,width=10,font='verdana  8 bold ',background='silver',fg='black')
            kembali.place(x=500,y=500)

        def in_Transaksi():
            Laundry.geometry('1000x900')
            #Laundry.config(background='black')

            self.Tombol_transaksi.destroy(),self.Tombol_logout.destroy(),self.Tombol_jenis_laundry.destroy(),self.Tombol_data_pelanggan.destroy()
            Teks1.destroy()

            Teks2=tk.Label(Laundry,text="...LAUNDRY...",font='Heltevica  35 bold italic')
            Teks2.place(x=200,y=0)

            Teks3=tk.Label(Laundry,text="Transaksi Laundry",font='Courier  15 bold')
            Teks3.place(x=250,y=60)

            labelframe1 = tk.LabelFrame(Laundry, text="Data Transaksi",bd=5)#bg='silver')
            labelframe1.place(x=0,y=85)
            #labelframe1.grid(column=10,padx=100,pady=150)
            labelframe1.grid_propagate(0)
            labelframe1.config(width=700,height=300)

            Teks_nama=tk.Label(labelframe1,text="NAMA",padx=5,pady=0)
            Teks_nama.grid(column=1,row=0,sticky='W')
            Entry_nama=tk.Entry(labelframe1,width=30)
            Entry_nama.grid(column=100,row=0,padx=50,pady=0)

            Teks_alamat=tk.Label(labelframe1,text="ALAMAT",padx=5,pady=0)#.place(x=0,y=190)
            Teks_alamat.grid(column=1,row=2,sticky='W')
            Entry_alamat=tk.Entry(labelframe1,width=30)
            Entry_alamat.grid(column=100,row=2,padx=153,pady=0)#place(x=100,y=193)

            Teks_no_hp=tk.Label(labelframe1,text="NO HP",padx=5,pady=0)
            Teks_no_hp.grid(column=1,row=3,sticky='W')
            Entry_no_hp=tk.Entry(labelframe1,width=30)
            Entry_no_hp.grid(column=100,row=3,padx=153,pady=0)#place(x=100,y=213)

            # labelframe2 = tk.LabelFrame(Laundry, text='Inputan',bd=5,bg='white')
            # labelframe2.place(x=0,y=250)
            # #labelframe2.grid(column=0,row=1,pady=0)#,padx=0,pady=500)
            # labelframe2.grid_propagate(0)
            # labelframe2.config(width=700,height=120)

            def fungsitampilharga(labelTampilHarga, pilihmenumakanan):
                menumakanan = pilihmenumakanan.get()
                if menumakanan == "sapo Tahu":
                    harga = 22000
                elif menumakanan == "Kailan Ham Jamur":
                    harga = 35000
                elif menumakanan == "Burger Vegetarian":
                    harga = 15000
                    labelTampilHarga.config(text=harga)
                return menumakanan
 
            Teks_jenis=tk.Label(labelframe1,text="JENIS LAUNDRY",padx=5,pady=0)
            Teks_jenis.grid(column=1,row=4,sticky='W')
            Entry_jenis=tk.Entry(labelframe1,width=30)
            Entry_jenis.grid(column=100,row=4,padx=95,pady=0)

            Teks_tgl_transaksi=tk.Label(labelframe1,text="TANGGAL TRANSAKSI",padx=5,pady=0)
            Teks_tgl_transaksi.grid(column=1,row=5,sticky='W')
            Entry_tgl_transaksi=tk.Entry(labelframe1,width=30)
            Entry_tgl_transaksi.grid(column=100,row=5,padx=95,pady=0)

            Teks_id_laundry=tk.Label(labelframe1,text="ID LAUNDRY",padx=5,pady=0)
            Teks_id_laundry.grid(column=1,row=6,sticky='W')
            Entry_id_laundry=tk.Entry(labelframe1,width=30)
            Entry_id_laundry.grid(column=100,row=6,padx=95,pady=0)

            Teks_berat_pakaian=tk.Label(labelframe1,text="BERAT PAKAIAN",padx=5,pady=0)
            Teks_berat_pakaian.grid(column=1,row=7,sticky='W')
            Entry_berat_pakaian=tk.Entry(labelframe1,width=30)
            Entry_berat_pakaian.grid(column=100,row=7,padx=95,pady=0)

            Teks_layanan_antar_jemput=tk.Label(labelframe1,text="LAYANAN ANTAR JEMPUT",padx=5,pady=0)
            Teks_layanan_antar_jemput.grid(column=1,row=8,sticky='W')
            Entry_layanan_antar_jemput=tk.Entry(labelframe1,width=30)
            Entry_layanan_antar_jemput.grid(column=100,row=8,padx=95,pady=0)

            Teks_total_harga=tk.Label(labelframe1,text="TOTAL HARGA",padx=5,pady=0)
            Teks_total_harga.grid(column=1,row=9,sticky='W')
            Entry_total_harga=tk.Entry(labelframe1,width=30)
            Entry_total_harga.grid(column=100,row=9,padx=95,pady=0)

            Teks_status=tk.Label(labelframe1,text="STATUS",padx=5,pady=0)
            Teks_status.grid(column=1,row=10,sticky='W')
            Entry_status=tk.Entry(labelframe1,width=30)
            Entry_status.grid(column=100,row=10,padx=95,pady=0)
            
            # def back():
            #     labelframe1.destroy(),Teks2.destroy(),Teks3.destroy(),tree.destroy()
            #     self.Menu()
            # kembali=tk.Button(Laundry,text='Back',command=back,width=10,font='verdana  8 bold ',background='silver',fg='black')
            # kembali.grid(row=10,column=2,pady=500)
            #kembali.place(x=500,y=400)

            # parent.grid_rowconfigure(0,weight=1)
            # parent.grid_columnconfigure(0,weight=1)
            # Frame1.grid_propagate(100)
            # Frame1.config(width=0,height=0)
           
            Frame = tk.Frame(Laundry)
            #Frame.pack(pady=20)
            Frame.place(y=300)
            Frame.config(height=1)

            # scrol=Scrollbar(Laundry,orient='horizontal')
            # #scrol.pack(side=RIGHT,fill=Y)
            # scrol.grid(column=0)

            tree=Treeview(Frame,columns=('#0','#1','#2','#3','#4','#5','#6','#7','#9'))
            # tree.heading('#0', text='No')
            tree.heading('#0', text='Nama')
            tree.heading('#1', text='Alamat')
            tree.heading('#2', text='No Hp')
            tree.heading('#3', text='Jenis')
            tree.heading('#4', text='Tanggal Transaksi')
            tree.heading('#5', text='Id Laundry')
            tree.heading('#6', text='Berat Pakaian')
            tree.heading('#7', text='Layanan Antar Jemput')
            tree.heading('#8', text='Harga')
            tree.heading('#9', text='Status')

            # tree.column('#0',stretch=YES,width=30,minwidth=30)
            tree.column('#0', stretch=YES,width=100,minwidth=100)
            tree.column('#1',width=100)
            tree.column('#2',stretch=YES,width=100)
            tree.column('#3',stretch=YES,width=100)
            tree.column('#4', stretch=YES,width=100)
            tree.column('#5', stretch=YES,width=100)
            tree.column('#6',stretch=YES,width=100)
            tree.column('#7',stretch=YES,width=100,minwidth=100)
            tree.column('#8',stretch=YES,width=100,minwidth=100)
            tree.column('#9',stretch=YES,width=100,minwidth=100)
            tree.grid(row=0,columnspan=1,pady=0,sticky='nsew')
             
            #scrol.config(command=tree.yview)
            treeview = tree
            def insert_data():
                #i = 1 
                # text=str(i)
                treeview.insert('', 'end',text=str(Entry_nama.get()),values=(Entry_alamat.get(),Entry_no_hp.get(),Entry_jenis.get(),Entry_tgl_transaksi.get(),Entry_id_laundry.get(),Entry_berat_pakaian.get(),Entry_layanan_antar_jemput.get(),Entry_total_harga.get(),Entry_status.get()))
                #i+=1 
            insert_button = tk.Button(Laundry, text = "Insert",padx=45,pady=2,font='verdana  8 bold ',bg='silver',command=insert_data)
            insert_button.grid(row = 1, column = 1,padx=0,pady=570,sticky='W') 

            def back():
                labelframe1.destroy(),Teks2.destroy(),Teks3.destroy(),tree.destroy()
                self.Menu()
            kembali_button=tk.Button(Laundry,text='Back',command=back,padx=50,pady=2,font='verdana  8 bold ',background='silver')
            kembali_button.grid(row=1,column=11,padx=0,pady=0)
        
            def remove():
                a=tree.selection()[0]  
                tree.delete(a)

            remove_button=tk.Button(Laundry,text='Delete',command=remove,padx=40,pady=2,font='verdana  8 bold ',background='silver')
            remove_button.grid(row=1,column=6,padx=140,pady=0)

            
           
            # tree.column('#0',width=30)
            # tree.column('#1',width=70,minwidth=100)
            # tree.column('#2',width=70,minwidth=100)
            # tree.column('#3',width=70,minwidth=100)
            # tree.column('#4',width=150,minwidth=100)
            # tree.column('#5',width=70,minwidth=100)
            # tree.column('#6',width=70,minwidth=100)
            # tree.column('#7',width=150,minwidth=100)
            
            # tree.heading('#0',text='Nomor')
            # tree.heading('#1',text='Nama')
            # tree.heading('#2',text='Alamat')
            # tree.heading('#3',text='No Hp')
            # tree.heading('#4',text='Tanggal Transaksi')
            # tree.heading('#5',text='Id Laundry')
            # tree.heading('#6',text='Berat Pakaian')
            # tree.heading('#7',text='Layanan Antar Jemput')
            # tree.grid(row=4, columnspan=4, sticky='nsew')
            # tree.insert('','end',values=(Entry_nama.get(), Entry_alamat.get(), Entry_id_pelanggan.get(), Entry_no_hp.get(), Entry_kode_layanan.get(), Entry_tgl_transaksi.get(), Entry_id_laundry.get(), Entry_berat_pakaian.get(), Entry_layanan_antar_jemput.get()))
            
            # insert_button = tk.Button(Laundry, text = "Insert",padx=50,pady=5,bg='pink',command=Teks_alamat)
            # insert_button.grid(row = 5, column = 0, sticky ="N",pady=170)
             
        
            # hbar = ttk.Scrollbar(Laundry, orient=HORIZONTAL, command=tree.xview)
            # tree.configure(xscrollcommand=hbar.set)
            # hbar.grid(row=3, column=0, sticky="EW")


        
        Teks1=tk.Label(Laundry,text="...LAUNDRY...",font='Heltevica  35 bold italic')#.pack()
        Teks1.place(x=200,y=60)
        
        self.Tombol_jenis_laundry=tk.Button(Laundry, text="Jenis Laundry",width=20,font='verdana  12 bold ',background='white',fg='black',command=in_jenis_laundry)#.pack()
        self.Tombol_jenis_laundry.place(x=240,y=150)
        
        self.Tombol_data_pelanggan=tk.Button(Laundry, text="Data Pelanggan",width=20,font='verdana  12 bold',background='white',fg='black')#.pack()
        self.Tombol_data_pelanggan.place(x=240,y=200)

        self.Tombol_transaksi=tk.Button(Laundry, text="Transaksi",width=20,font='verdana  12 bold',background='white',fg='black',command=in_Transaksi)
        self.Tombol_transaksi.place(x=240,y=250)

        self.Tombol_logout=tk.Button(Laundry, text="LOG OUT",font='verdana  12 bold ',width=20,background='white',fg='black',command=self.Exit)#.pack()
        self.Tombol_logout.place(x=240,y=300)   

Laundry.geometry('700x600')
Laundry.title('Laundry')
j=jenis()
Laundry.mainloop()


#font_teks= Font(family='Heltevica',size=10,weight='bold',slant='roman')
# Teks1=tk.Label(Laundry,text="...LAUNDRY...",font='Heltevica  16 bold italic')
# Teks1.pack()
#Teks1.grid(row=0,column=10)

