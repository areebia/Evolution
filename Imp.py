import Race

class Imp(Race.Race):
   
    def __init__(self, exp = 0, amount = 1):
        self.name = "Imp" 
        self.hp = 10
        self.atk = 1.5
        self.defense = 1.5
        self.atkSpd = 3.2
        self.intel = .3
        self.birRate = .35
        self.evo = 25
        self.exp = exp
        self.tier = 1
        self.amount = amount

   
class Baron(Imp):
    def __init__(self, exp = 0, amount = 1):
        self.name = "Baron" 
        self.hp = 50
        self.atk = 6
        self.defense = 4
        self.atkSpd = 3.2
        self.intel = .35
        self.evo = 80
        self.exp = exp
        self.tier = 2
        self.amount = amount

class Count(Imp):
    def __init__(self, exp = 0, amount = 1):
        self.name = "Count" 
        self.hp = 100
        self.atk = 10
        self.defense = 5
        self.atkSpd = 3.2
        self.intel = .45
        self.evo = 175
        self.exp = exp
        self.tier = 3
        self.amount = amount

class Marquis(Imp):
    def __init__(self, exp = 0, amount = 1):
        self.name = "Marquis" 
        self.hp = 175
        self.atk = 14
        self.defense = 7
        self.atkSpd = 3.2
        self.intel = .55
        self.evo = 1500
        self.exp = exp
        self.tier = 4
        self.amount = amount

class Duke(Imp):
    def __init__(self, exp = 0, amount = 1):
        self.name = "Duke" 
        self.hp = 250
        self.atk = 20
        self.defense = 10
        self.atkSpd = 3.55
        self.intel = .7
        self.exp = exp
        self.tier = 5
        self.amount = amount