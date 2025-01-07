'''
static method ->bisa diakses dengan class dan object/instance

class method -> bisa diakses dengan class dan object/instance
'''


class Kucing:
    
    # class variable
    __hidup = True
    __kaki = 4
    __suara = "meow"
    __japan_name = "neko"

    def __init__(self, jenis, warna):
        self.__jenis = jenis
        self.__warna = warna

    ## method ini hanya berlaku pada object
    def get_hidup(self):
        return Kucing.__hidup
    
    ## method ini hanya berlaku pada class
    def get_kaki():
        return Kucing.__kaki
    
    # static method
    @staticmethod
    def get_suara():
        return Kucing.__suara
    
    # class method
    @classmethod
    def get_japan_name(cls):
        return cls.__japan_name

sumbul = Kucing("anggora", "orange")

## testing

#1
print(sumbul.get_hidup())
# print(Kucing.get_hidup()) -> eror

#2
# print(sumbul.get_kaki()) -> eror
print(Kucing.get_kaki())

#3
print(sumbul.get_suara())
print(Kucing.get_suara())

#4
print(sumbul.get_japan_name()) 
print(Kucing.get_japan_name())
