'''
Dalam Object-Oriented Programming (OOP) di Python, abstract class adalah kelas dasar yang tidak dimaksudkan untuk dibuat instansnya secara langsung, melainkan menjadi template bagi kelas-kelas turunannya. Abstract class memiliki metode atau fungsi yang dideklarasikan tetapi belum diimplementasikan. Tujuannya adalah memaksa kelas turunannya untuk menyediakan implementasi konkret dari metode-metode tersebut.
'''

from abc import ABC, abstractmethod

class Hewan(ABC): # artinya ini adalah abstrack class
    
    @abstractmethod
    def get_status(self): # memaksa semua child dari class ini mempunyai method get_status()
        pass              # jika tidak ada, maka akan eror
    
class Nyamuk(Hewan):
    def __init__(self, status):
        self.status = status
        
    def get_status(self):
        return f"status = {self.status}"

# class Isriwil(Hewan):
#     def __init__(self, status):
#         self.status = status  -> bakal menyebabkan eror karena tidak ada fungsi get_status()
        
    
    
# isriwil = Isriwil("mati")
nyamuk = Nyamuk("mati")
print(nyamuk.get_status())