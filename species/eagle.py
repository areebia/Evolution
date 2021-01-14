import Race

class Eagle(Race.Race):
   
    def __init__(self, exp = 0, amount = 1):
        self.name = "Eagle" 
        self.hp = 25
        self.atk = 3
        self.defense = 1.75
        self.atkSpd = 3.5
        self.intel = .15
        self.birRate = .35
        self.evo = 30
        self.exp = exp
        self.tier = 1
        self.amount = amount

   
class GEagle(Eagle):
    def __init__(self, exp = 0, amount = 1):
        self.name = "Giant Eagle" 
        self.hp = 60
        self.atk = 6
        self.defense = 3.5
        self.atkSpd = 3.5
        self.intel = .2
        self.evo = 75
        self.exp = exp
        self.tier = 2
        self.amount = amount

class SEagle(Eagle):
    def __init__(self, exp = 0, amount = 1):
        self.name = "Snowy Eagle" 
        self.hp = 100
        self.atk = 9
        self.defense = 5.5
        self.atkSpd = 3.5
        self.intel = .275
        self.evo = 200
        self.exp = exp
        self.tier = 3
        self.amount = amount

class GFEagle(Eagle):
    def __init__(self, exp = 0, amount = 1):
        self.name = "Giant Frost Eagle" 
        self.hp = 175
        self.atk = 13
        self.defense = 9.5
        self.atkSpd = 3.5
        self.intel = .35
        self.evo = 1300
        self.exp = exp
        self.tier = 4
        self.amount = amount

class Griffin(Eagle):
    def __init__(self, exp = 0, amount = 1):
        self.name = "Griffin" 
        self.hp = 350
        self.atk = 17
        self.defense = 15.5
        self.atkSpd = 3.75
        self.intel = .55
        self.exp = exp
        self.tier = 5
        self.amount = amount