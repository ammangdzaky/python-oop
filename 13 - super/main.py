class Hero:
    def __init__(self, name, health):
        self.name = name
        self.health = health


    def info(self):
        return f"\ninfo: \nname = {self.name} \nhealth = {self.health}"
    
    
# misal health default untuk mm yaitu 100
class Marksman(Hero):
    
    # def __init__(self, name,):
    #     self.name = name
    #     self.health = 100 -> cara panjang untuk koroco
    
    # def __init__(self, name):
    #     Hero.__init__(self, name, 100) -> lumayan pendek tapi kroco
    
    def __init__(self, name):
        super().__init__(name,100) # rekomend
        
        super().info()


# misal health default untuk tank yaitu 100
class Tank(Hero):
    
    def __init__(self, name):
        super().__init__(name,200)
        super().info()

layla = Marksman("Layla")
tigreal = Tank("Tigreal")

print(f"{layla.name} -> health = {layla.health}")
print(f"{tigreal.name} -> health = {tigreal.health}")
print(layla.info())
print(tigreal.info())