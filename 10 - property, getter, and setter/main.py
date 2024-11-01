'''
class Hero:
    
    def __init__(self, name, health):
        self.__name = name
        self.__health = health
        
    def get_name(self):
        return self.__name
    
    @property
    def health(self):
        pass
    
    @health.getter
    def health(self):
        return self.__health
    
alucard = Hero("alucard", 100)

print(alucard.get_name()) --> getter biasa / cupu
print(alucard.health)     --> getter python / suhu
'''

class Laptop:
    
    def __init__(self, merek, warna, ram):
        self.__merek = merek
        self.__warna = warna
        self.__ram = ram
        
    @property
    def spek(self): # ini method tapi dipanggil malah kayak atribut, misal print(asus.spek), bukan print(asus.spek())
        return f"===\nmerek = {self.__merek}\nram = {self.__ram}\n==="
    
    @property
    def warna(self):
        pass
    
    # getter 
    @warna.getter
    def warna(self):
        return self.__warna
    
    # setter
    @warna.setter
    def warna(self, value):
        self.__warna = value
        
    # deleter
    @warna.deleter
    def warna(self):
        self.__warna = None
        
tetora = Laptop("Advan", "putih", 16)

# panggil fungsi spek
print(tetora.spek)

# panggil fungsi getter
print(tetora.warna)

# fungsi setter
tetora.warna = "hitam"

# panggil fungsi getter lagi
print(tetora.warna)

# panggil fungsi deleter
del tetora.warna

# panggil fungsi getter lagi
print(tetora.warna)