'''
class contoh:
    
    def __init__(self, x):    self -> variable, x -> arguments
    
contoh_satu = contoh("a")

self -> contoh_satu, dan seterusnya

x    -> "a", dan seterusnya 
'''

class hero:
    def __init__(self, name, power, health, defense):
        self.name = name
        self.power = power
        self.health = health
        self.defense = defense
        
# saya kemudian membuat objectnya

hero_satu = hero("alucard", 100, defense=200, health=100) 
hero_dua = hero("angela", 200, 100, 300)


# saya ambil

print("\n")

print(hero_satu.__dict__) # -> menampilkan semua atribut pada object hero_satu

print(hero_satu.defense)

print(hero_dua.name)

print(hero_dua.defense)

print("\n")