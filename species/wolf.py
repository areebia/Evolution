import Race

class Wolf(Race.Race):
   
    def __init__(self, exp = 0, amount = 1):
        self.name = "Wolf" 
        self.hp = 25
        self.atk = 3.5
        self.defense = 3
        self.atkSpd = 3.5
        self.intel = .15
        self.birRate = .25
        self.evo = 35
        self.exp = exp
        self.tier = 1
        self.amount = amount 
   
class GreyWolf(Wolf):
    def __init__(self, exp = 0, amount = 1):
        self.name = "Grey Wolf" 
        self.hp = 75
        self.atk = 6.5
        self.defense = 6
        self.atkSpd = 3.5
        self.intel = .25
        self.evo = 100
        self.exp = exp
        self.tier = 2
        self.amount = amount 

class DuskWolf(Wolf):
    def __init__(self, exp = 0, amount = 1):
        self.name = "Dusk Wolf" 
        self.hp = 125
        self.atk = 10
        self.defense = 8.5
        self.atkSpd = 3.5
        self.intel = .3
        self.evo = 200
        self.exp = exp
        self.tier = 3
        self.amount = amount 

class WereWolf(Wolf):
    def __init__(self, exp = 0, amount = 1):
        self.name = "Werewolf" 
        self.hp = 200
        self.atk = 13.5
        self.defense = 10.5
        self.atkSpd = 3.5
        self.intel = .45
        self.evo = 1300
        self.exp = exp
        self.tier = 4
        self.amount = amount 

class Lycan(Wolf):
    def __init__(self, exp = 0, amount = 1):
        self.name = "Lycan" 
        self.hp = 300
        self.atk = 18
        self.defense = 16
        self.atkSpd = 3.75
        self.intel = .7
        self.exp = exp
        self.tier = 5
        self.amount = amount 