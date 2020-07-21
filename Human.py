import Race

class Human(Race.Race):
   
    def __init__(self, exp = 0, amount = 1):
        self.name = "Human" 
        self.hp = 50
        self.atk = 3
        self.defense = 2
        self.atkSpd = 2
        self.intel = .45
        self.birRate = .3
        self.evo = 50
        self.exp = exp
        self.tier = 1
        self.amount = amount

   
class Warrior(Human):
    def __init__(self, exp = 0, amount = 1):
        self.name = "Warrior" 
        self.hp = 100
        self.atk = 6
        self.defense = 5
        self.atkSpd = 2
        self.intel = .45
        self.evo = 100
        self.exp = exp
        self.tier = 2
        self.amount = amount

class Swordsman(Human):
    def __init__(self, exp = 0, amount = 1):
        self.name = "Swordsman" 
        self.hp = 150
        self.atk = 9
        self.defense = 7
        self.atkSpd = 2
        self.intel = .55
        self.evo = 200
        self.exp = exp
        self.tier = 3
        self.amount = amount

class Knight(Human):
    def __init__(self, exp = 0, amount = 1):
        self.name = "Knight" 
        self.hp = 200
        self.atk = 12
        self.defense = 9
        self.atkSpd = 2
        self.intel = .6
        self.evo = 1000
        self.exp = exp
        self.tier = 4
        self.amount = amount

class King(Human):
    def __init__(self, exp = 0, amount = 1):
        self.name = "King" 
        self.hp = 300
        self.atk = 16
        self.defense = 13
        self.atkSpd = 2
        self.intel = .75
        self.exp = exp
        self.tier = 5
        self.amount = amount
