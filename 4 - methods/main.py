class mc:

    #variable class
    jumlah = 0
    
    def __init__(self, name, health, power, mewinglevel):
        self.name = name
        self.health = health
        self.power = power
        self.mewing = mewinglevel
        
        mc.jumlah += 1
        
    
    #method tampa arguments / void method
    def siapa(self): # -> self disini bukan argument, tapi variable
        print(f"namaku adalah {self.name}")
        
    #method dengan arguments
    def powerup(self, up):
        self.power += up
        print(f"power {self.name} sekarang yaitu : {self.power}")

    #methods dengan return
    def getMewing(self):
        return self.mewing
    
    
mc_1 = mc("atomic", 100, 100, 5)
mc_2 = mc("jojo", 10, 10, 100)
mc_3 = mc("subadrun", 1, 1, 999)

mc_1.siapa()
print(mc_2.getMewing())
mc_3.powerup(999)
