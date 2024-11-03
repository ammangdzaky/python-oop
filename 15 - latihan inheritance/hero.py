class Hero:
    def __init__(self, name):
        self.__name = name
        self.health_pool = []
        self.attack_pool = []
        self.armor_pool = []
        self.__level = 0
        self.__exp = 0
        
    def info(self):
        return f'''
    {self.__name}
        level   = {self.__level}
        health  = {self.__health}
        attack  = {self.__attack}
        armor   = {self.__armor}
    '''
    
    @property
    def health_pool(self):
        pass
    
    @property
    def attack_pool(self):
        pass
    
    @property
    def armor_pool(self):
        pass
    
    @property
    def exp_up(self):
        pass
    
    @property
    def level_up(self):
        pass
    
    @health_pool.setter
    def health_pool(self, value):
        self.__health_pool = value

    @attack_pool.setter
    def attack_pool(self, value):
        self.__attack_pool = value

    @armor_pool.setter
    def armor_pool(self, value):
        self.__armor_pool = value
    
    @exp_up.setter
    def exp_up(self, value):
        self.__exp += value
        if self.__exp > 100:
            self.level_up = self.__exp // 100
            self.__exp = self.__exp // 100
            
    @level_up.setter
    def level_up(self, value):
        self.__level += value
        if self.__level >= len(self.__health_pool):
            self.__level = len(self.__health_pool) - 1
        self.__health = self.__health_pool[self.__level]
        self.__attack = self.__attack_pool[self.__level]
        self.__armor = self.__armor_pool[self.__level]
        

class Assasin(Hero):
    def __init__(self,name):
        super().__init__(name)
        self.health_pool = [0,50,100,150,200,250,300,350,400,450,500]
        self.attack_pool = [0,20,40,60,80,100,120,140,160,180,200]
        self.armor_pool = [0,5,10,15,20,25,30,35,40,50,55]
        self.level_up = 1

        
class Tank(Hero):
    def __init__(self,name):
        super().__init__(name)
        self.health_pool = [0,100,200,300,400,500,600,700,800,900,1000]
        self.attack_pool = [0,5,10,15,20,25,30,35,40,50,55]
        self.armor_pool = [0,20,40,60,80,100,120,140,160,180,200]
        self.level_up = 1