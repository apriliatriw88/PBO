# from tkinter import*

# root = Tk()
# w = Label(root, text='Hello World')
# w.pack()
# root.mainloop()

# def show_entry_field():
#     print('Selamat Siang, %s'%(e.get()))
#     e.delete(0, END)

# master = Tk()
# Label(master, text='Kelas PBO Python!').grid(row=0, column=0)
# Label(master, text='Nama Lengkap').grid(row=1)

# e = Entry(master)
# e.grid(row=1,column=1)

# Button(master, text='salam', command=show_entry_field).grid(row=3, column=0, sticky=W, pady=4)
# Button(master, text='keluar', command=master.quit).grid(row=3, column=1, sticky=W, pady=4)

# mainloop()


# import tkinter as tk
# window = tk.Tk()
# window.title('menghitung perkalian')


# e1 = tk.Label(window, text='suhu celcius : ')
# e1.grid(column=0, row=0)

# e2 = tk.Entry(window, width=20)
# e2.grid(column=1, row=0)

# def luas() :
#     alas = 'suhu awal celcius : %s'%(e2.get())

#     tk.Label(window, text= alas).grid(row=3, columnspan=1)
#     hasil.configure(text=(float(e2.get())*(9/5)+32))

# BTN =tk.Button(window, text='suhu f', width=10, command=luas)
# BTN.grid(column=1, row=3, pady=14)

# tk.mainloop()





# from tkinter import *

# bd = Tk()
# bd.title("Menghitung Luas Bangun 2D")
# bd.geometry("200x150")

# a,b,triangle3 = IntVar(),IntVar(),DoubleVar()

# def triangle_area():
#     try:
#         triangle3.set(round(float((a.get()*b.get())/2),2))
#         Label(text = "L.Segitiga:").grid(row = 4, column = 0)
#         Label(bd, textvariable = triangle3).grid(row = 4, column = 1)
#     except ValueError:
#         pass

# #display
# Label(bd, text ="Luas Segitiga").grid(row = 0, column = 1)
# Label(bd, text = "Alas\t:").grid(row = 1, column = 0)
# Entry(bd, textvariable = a).grid(row= 1, column = 1)
# Label(bd, text = "Tinggi\t:").grid(row = 2, column = 0)
# Entry(bd, textvariable = b).grid(row = 2, column = 1)
# Button(bd, text = "Hasil",command = triangle_area).grid(row = 3, column = 1)

# bd.mainloop()

# "Menggunakan PBO"

# from tkinter import *

# class Triangle:
    
#     def __init__(self,sub_master):
#         self.sub_master = sub_master
#         self.sub_frame = Frame(self.sub_master)
#         self.sub_frame.pack()
#         self.sub_master.title("SEGITIGA")
#         self.sub_master.geometry("200x200")
            
#         self.a = DoubleVar()
#         self.t = DoubleVar()
#         self.luas3 = DoubleVar()

#         self.label1 = Label(self.sub_frame,text = "Nilai Alas:")
#         self.label1.grid(row= 0,column = 0)
#         self.entry1 = Entry(self.sub_frame,textvariable = self.a)
#         self.entry1.grid(row = 0,column = 1)    
#         self.label2 =  Label(self.sub_frame,text = "Nilai Tinggi:")
#         self.label2.grid(row= 1,column = 0)    
#         self.entry2 = Entry(self.sub_frame,textvariable = self.t)
#         self.entry2.grid(row = 1,column = 1)
#         self.hitung = Button(self.sub_frame, text = "Hitung",command = self.hitung_luas3)
#         self.hitung.grid(row = 2, column =1)
#         self.selesai = Button(self.sub_frame, text = "Selesai",command = self.sub_master.destroy)
#         self.selesai.grid(row = 2,column = 0)

#     def hitung_luas3(self):
#         try:
#             self.luas3.set(round(float((self.a.get()*self.t.get())/2),2))
#             self.label3 = Label(self.sub_frame,text = "L.Segi3 = ")
#             self.label3.grid(row = 3,column = 0)
#             self.label4 = Label(self.sub_frame, textvariable = self.luas3)
#             self.label4.grid(row = 3, column = 1)
#         except ValueError:
#             pass

# def main_program():
#     bd = Tk()
#     Triangle(bd)
#     bd.mainloop()

# main_program()







# no 1 dan 2
import tkinter as tk
master = tk.Tk()
master.title('mahasiswa')

tk.Label(master, text='nama : ').grid(row=0)
tk.Label(master, text='nim : ').grid(row=1)
tk.Label(master, text='prodi : ').grid(row=2)

nam= tk.Entry(master)
n=tk.Entry(master)
pd=tk.Entry(master)

nam.grid(row=0, column=2)
n.grid(row=1, column=2)
pd.grid(row=2, column=2)

def tampil():
    txt_nama = 'nama : %s'%(nam.get())
    txt_nim = 'nim : %s'%(n.get())
    txt_pd = 'prodi : %s'%(pd.get())
    tk.Label(master, text=txt_nama).grid(row=4, columnspan=2)
    tk.Label(master, text=txt_nim).grid(row=5, columnspan=2)
    tk.Label(master, text=txt_pd).grid(row=6, columnspan=2)

btampil = tk.Button(master, text='tampil', command=tampil)
btampil.grid(row=3, column=0, sticky=tk.W, pady=4)

tk.mainloop()


# versi output diterminal
master = tk.Tk()
master.title('mahasiswa')

tk.Label(master, text='nama : ').grid(row=0)
tk.Label(master, text='nim : ').grid(row=1)
tk.Label(master, text='prodi : ').grid(row=2)

nam= tk.Entry(master)
n=tk.Entry(master)
pd=tk.Entry(master)

nam.grid(row=0, column=2)
n.grid(row=1, column=2)
pd.grid(row=2, column=2)

def tampil():
    print('nama : %s'%(nam.get()))
    print('nim : %s'%(n.get()))
    print('prodi : %s'%(pd.get()))


btampil = tk.Button(master, text='tampil', command=tampil)
btampil.grid(row=3, column=0, sticky=tk.W, pady=4)

tk.mainloop()


# import tkinter as tk
# master = tk.Tk()
# master.title('mahasiswa')

# tk.Label(master, text='nama : ').grid(row=0)
# tk.Label(master, text='nim : ').grid(row=1)
# tk.Label(master, text='prodi : ').grid(row=2)

# n = tk.Entry(master)
# nm = tk.Entry(master)
# p = tk.Entry(master)

# n.grid(row=0, column=2)
# nm.grid(row=1, column=2)
# p.grid(row=2, column=2)

# def tampil() :
#     print('nama : %s'%(n.get()))
#     print('nim : %s'%(nm.get()))
#     print('prodi : %s'%(p.get()))
    
# btmp = tk.Button(master, text='tampil', command=tampil)
# btmp.grid(row=3, column=0, sticky=tk.W, pady=4)
# tk.mainloop()
