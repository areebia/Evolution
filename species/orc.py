import Race

class Orc(Race.Race):
   
    def __init__(self, exp = 0, amount = 1):
        self.name = "Orc" 
        self.hp = 100
        self.atk = 4
        self.defense = 3
        self.atkSpd = 1
        self.intel = .2
        self.birRate = .25
        self.evo = 65
        self.exp = exp
        self.tier = 1
        self.amount = amount

   
class HOrc(Orc):
    def __init__(self, exp = 0, amount = 1):
        self.name = "High Orc" 
        self.hp = 200
        self.atk = 6
        self.defense = 6
        self.atkSpd = 1
        self.intel = .25
        self.evo = 130
        self.exp = exp
        self.tier = 2
        self.amount = amount

class OrcL(Orc):
    def __init__(self, exp = 0, amount = 1):
        self.name = "Orc Lieutenant" 
        self.hp = 300
        self.atk = 8
        self.defense = 9
        self.atkSpd = 1
        self.intel = .3
        self.evo = 275
        self.exp = exp
        self.tier = 3
        self.amount = amount

class OrcC(Orc):
    def __init__(self, exp = 0, amount = 1):
        self.name = "Orc Captain" 
        self.hp = 400
        self.atk = 11
        self.defense = 14
        self.atkSpd = 1
        self.intel = .4
        self.evo = 1500
        self.exp = exp
        self.tier = 4
        self.amount = amount

class OrcG(Orc):
    def __init__(self, exp = 0, amount = 1):
        self.name = "Orc General" 
        self.hp = 500
        self.atk = 15
        self.defense = 20
        self.atkSpd = 1.5
        self.intel = .5
        self.exp = exp
        self.tier = 5
        self.amount = amount