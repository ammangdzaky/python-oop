class Pecahan:
    def __init__(self, pembilang, penyebut):
        if  not isinstance(pembilang, int):
            raise TypeError("must Integer!!!")
        if  not isinstance(pembilang, int):
            raise TypeError("must Integer!!!")
        if penyebut == 0:
            raise ValueError("penyebut tidak boleh 0!!!")
        
        self.pembilang = pembilang
        self.penyebut = penyebut
        
        
    def __str__(self):
        return f"{self.pembilang}/{self.penyebut}"


    def __add__(self, other):
        if self.penyebut != self.penyebut:
            pembilang_baru = (self.penyebut * other.penyebut) + (self.pembilang * other.penyebut)
            penyebut_baru = self.penyebut * other.penyebut
            return Pecahan(pembilang_baru, penyebut_baru)
        else:
            pembilang_baru = self.pembilang + other.pembilang
            return Pecahan(pembilang_baru, self.penyebut)

        
    def __sub__(self, other):
        if self.penyebut != self.penyebut:
            pembilang_baru = (self.penyebut * other.penyebut) - (self.pembilang * other.penyebut)
            penyebut_baru = self.penyebut * other.penyebut
            return Pecahan(pembilang_baru, penyebut_baru)
        else:
            pembilang_baru = self.pembilang - other.pembilang
            return Pecahan(pembilang_baru, self.penyebut)


    
    def kali(self, other):
        pembilang_baru = self.pembilang * other.pembilang
        penyebut_baru = self.penyebut * other.penyebut
        return Pecahan(pembilang_baru, penyebut_baru)


    def bagi(self, other):
        pembilang_baru = self.pembilang * other.penyebut
        penyebut_baru = self.penyebut * other.pembilang
        return Pecahan(pembilang_baru, penyebut_baru)



    def sederhanakan(self):
        # Cari FPB (Faktor Pembagi Terbesar) dengan cara sederhana
        def fpb(a, b):
            while b != 0:
                a, b = b, a % b
            return a
        
        # Hitung FPB pembilang dan penyebut
        faktor_pembagi = fpb(self.pembilang, self.penyebut)
        
        # Bagi pembilang dan penyebut dengan FPB
        pembilang_sederhana = self.pembilang // faktor_pembagi
        penyebut_sederhana = self.penyebut // faktor_pembagi
        
        return Pecahan(pembilang_sederhana, penyebut_sederhana)


pecahan_a = Pecahan(1,3)
pecahan_b = Pecahan(2,3)
print(pecahan_a)
print(pecahan_b)
print(pecahan_a + pecahan_b)
print(pecahan_a - pecahan_b)
print(pecahan_a.kali(pecahan_b))
print(pecahan_a.bagi(pecahan_b))
print((pecahan_a.bagi(pecahan_b)).sederhanakan())