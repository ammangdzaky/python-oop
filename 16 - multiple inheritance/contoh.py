class Team:
    def set_team(self,team):
        self.team = team
    def show_team(self):
        return self.team
    
class Role:
    def set_role(self,role):
        self.role = role
    def show_role(self):
        return self.role
    
class Hero(Team, Role):
    def __init__(self, name, health):
        self.name = name
        self.health = health
        
alucrot = Hero("Alucrot", 100)

alucrot.set_team("epos")
alucrot.set_role("mm")

print(alucrot.show_team())
print(alucrot.show_role())