import Race

class Angel(Race.Race):
   
    def __init__(self, exp = 0, amount = 1):
        self.name = "Angel" 
        self.hp = 75
        self.atk = 5
        self.defense = 5
        self.atkSpd = 2
        self.intel = .55
        self.birRate = .05
        self.evo = 100
        self.exp = exp
        self.tier = 1
        self.amount = amount

   
class HighAngel(Angel):
    def __init__(self, exp = 0, amount = 1):
        self.name = "High Angel" 
        self.hp = 125
        self.atk = 9.5
        self.defense = 8.5
        self.atkSpd = 2
        self.intel = .65
        self.evo = 200
        self.exp = exp
        self.tier = 2
        self.amount = amount

class Throne(Angel):
    def __init__(self, exp = 0, amount = 1):
        self.name = "Throne" 
        self.hp = 175
        self.atk = 13
        self.defense = 12
        self.atkSpd = 2
        self.intel = .75
        self.evo = 400
        self.exp = exp
        self.tier = 3
        self.amount = amount

class Cherubim(Angel):
    def __init__(self, exp = 0, amount = 1):
        self.name = "Cherubim" 
        self.hp = 225
        self.atk = 16
        self.defense = 14
        self.atkSpd = 2
        self.intel = .85
        self.evo = 1750
        self.exp = exp
        self.tier = 4
        self.amount = amount

class Seraphim(Angel):
    def __init__(self, exp = 0, amount = 1):
        self.name = "Seraphim" 
        self.hp = 400
        self.atk = 20
        self.defense = 16
        self.atkSpd = 2
        self.intel = .65
        self.exp = exp
        self.tier = 5
        self.amount = amount
