class Polygon :
    def __init__(self, banyak_sisi):
        self.n =banyak_sisi
        self.sisi = [0 for i in range(banyak_sisi)]

    def inputSisi(self) :
        print("masukan panjang sisi (dalam cm):")
        self.sisi = [float(input("sisi "+str(i+1)+" : ")) for i in range(self.n)]
        print()

    def dispSisi(self):
        for i in range(self.n) :
            print("panjang sisi", i+1,"adalah",self.sisi[i],"cm")
            print()

class segiEmpat(Polygon):
    def __init__(self) :
        Polygon.__init__(self,4)
        print("segiempat")
    def hitungKeliling(self):
        a,b,c,d = self.sisi
        k = a+b+c+d
        print("keliling segiempat adalah",k,"cm. ")

poligon = Polygon(4)
poligon.inputSisi()
poligon.dispSisi()

s4=segiEmpat()
s4.inputSisi()
s4.dispSisi()
s4.hitungKeliling()
