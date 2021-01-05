import Race

class Serpent(Race.Race):
   
    def __init__(self, exp = 0, amount = 1):
        self.name = "Serpent" 
        self.hp = 20
        self.atk = 3
        self.defense = 2
        self.atkSpd = 2.5
        self.intel = .15
        self.birRate = .4
        self.evo = 30
        self.exp = exp
        self.tier = 1
        self.amount = amount

   
class Python(Serpent):
    def __init__(self, exp = 0, amount = 1):
        self.name = "Python" 
        self.hp = 75
        self.atk = 5
        self.defense = 5.5
        self.atkSpd = 2.5
        self.intel = .2
        self.evo = 75
        self.exp = exp
        self.tier = 2
        self.amount = amount

class Viper(Serpent):
    def __init__(self, exp = 0, amount = 1):
        self.name = "Viper" 
        self.hp = 120
        self.atk = 9
        self.defense = 7
        self.atkSpd = 2.5
        self.intel = .3
        self.evo = 180
        self.exp = exp
        self.tier = 3
        self.amount = amount

class Cobra(Serpent):
    def __init__(self, exp = 0, amount = 1):
        self.name = "Cobra" 
        self.hp = 150
        self.atk = 13
        self.defense = 9.5
        self.atkSpd = 2.5
        self.intel = .45
        self.evo = 1250
        self.exp = exp
        self.tier = 4
        self.amount = amount

class Basilisk(Serpent):
    def __init__(self, exp = 0, amount = 1):
        self.name = "Basilisk" 
        self.hp = 250
        self.atk = 20
        self.defense = 10
        self.atkSpd = 2.75
        self.intel = .7
        self.exp = exp
        self.tier = 5
        self.amount = amount