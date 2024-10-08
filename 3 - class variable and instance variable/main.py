
class hero:
    # class varible
    jumlah = 0
    
    def __init__(self, name, power=0, health=0, defense=0):

        # instance variable / object atributs
        self.name = name
        self.power = power
        self.health = health
        self.defense = defense
        
        #memanipusali  class variable
        
        hero.jumlah += 1

        # artinya setiap memnbuat objek batu maka akan bertambah 1
        
        #setiap membuat object maka print
        
        print(f"membuat hero dengan nama : {self.name}")
        
hero_satu = hero("natalia")
print(hero.jumlah)
hero_dua = hero("alucard")
print(hero.jumlah)
hero_tiga = hero("hayabusa")
print(hero.jumlah)

        
        