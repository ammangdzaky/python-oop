'''
ENCAPSULASI

-> buat semua variable privat
-> getter => mengambil variabel
-> setter => mensetting variable

misal dibawa:
saya ingin agar nilai name, health, dan attack tidak bisa diotak atik dari luar

'''

class Hero:
    
    def __init__(self, name, health, attack):
        # variable privat (__xxx) agar tidak diotak atik
        self.__name = name 
        self.__health = health
        self.__attack = attack
        
    # getter
    def get_name(self):
        return self.__name
    def get_health(self):
        return self.__health
    def get_attack(self):
        return self.__attack
    
    # setter
    def diserang(self, enemy_attack):
        self.__health -= enemy_attack
    def critical_attack(self, crit):
        self.__attack += crit
    
    '''
    privat variable hanya bisa diotak atik di dalam class
    '''

alucrot = Hero("alucrot", 100, 10)

# print(alucrot.__name) -> bakal eror (mencoba mengakses privat variable diluar class)

print(alucrot.get_name())

# alucrot kemudian diserang 
alucrot.diserang(50)
print(f"sisa hp alucrot = {alucrot.get_health()}")

# tetapi alucrot menerima pedang zeus
alucrot.critical_attack(90)
print(f"damage serangan alucrot selanjutnya = {alucrot.get_attack()}")