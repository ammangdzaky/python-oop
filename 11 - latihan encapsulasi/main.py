#### SIMULASI MOBILE LEGEND ANJAYYY

class Hero:
    
    def __init__(self, name, health, power, armor):
        self.__name = name
        self.__defaultHealth = health
        self.__defaultPower = power
        self.__defaultArmor = armor
        self.__defaultLevel = 1
        self.__defaultExp = 0
        
        self.__healthNow = self.__defaultHealth * self.__defaultLevel
        self.__powerNow = self.__defaultPower * self.__defaultLevel
        self.__armorNow = self.__defaultArmor * self.__defaultLevel

    @property
    def additional_exp(self):
        pass
    
    @additional_exp.setter
    def additional_exp(self, value):
        if self.__defaultLevel < 15:
            self.__defaultExp += value
            if self.__defaultExp > 100:
                
                print(f"{self.__name} LEVEL UP!!")
                
                self.__defaultLevel += 1
                
                self.__healthNow = self.__defaultHealth * self.__defaultLevel*0.5
                self.__powerNow = self.__defaultPower * self.__defaultLevel
                self.__armorNow = self.__defaultArmor * self.__defaultLevel
                
                self.__defaultExp -= 100
            
    @property
    def info(self):
        return f"{self.__name} \n\thealth now = {self.__healthNow} \n\tpower now = {self.__powerNow} \n\tarmor now = {self.__armorNow}"
    
    def attack(self, enemy):
        if self.__defaultLevel < 15:
            self.additional_exp = 40
        enemy.attacked(self)
    
    def attacked(self, enemy):
        self.__healthNow -= enemy.__powerNow
        print(f"heath {self.__name} = {self.__healthNow}")
        if self.__healthNow <= 0:
            print(f"{self.__name} DEATH !!!")

    # @property
    # def health(self):
    #     pass
    # @health.getter
    # def health(self):
    #     return self.__healthNow  -> syntaks ini bisa disingkat
    
    @property
    def health(self):
        return self.__healthNow
    
# summon hero
alucard = Hero("Alucard", 100, 10, 15)
saber = Hero("Saber", 100, 15, 9)


# # GAME PLAY

while True:
    alucard.attack(saber)
    saber.attack(alucard)
    if saber.health <= 0 or alucard.health <= 0:
        break
    
    
    
    
    # if saber.health <= 0:
    #     print(alucard.info)
    #     break
    # if alucard.health <= 0:
    #     print(saber.info)
    #     break

# max_rounds = 100  # misalnya batas maksimal 100 putaran
# current_round = 0

# while current_round < max_rounds:
#     alucard.attack(saber)
#     if saber.health <= 0:
#         print(alucard.info)
#         break
#     saber.attack(alucard)
#     if alucard.health <= 0:
#         print(saber.info)
#         break
#     current_round += 1
# else:
#     print("Pertarungan berakhir dalam hasil draw.")
#     print(alucard.health)
#     print(saber.health)