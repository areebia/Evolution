import Race

class Zombie(Race.Race):
   
    def __init__(self, exp = 0, amount = 1):
        self.name = "Zombie" 
        self.hp = 40
        self.atk = 2.5
        self.defense = 3.5
        self.atkSpd = 1.75
        self.intel = .05
        self.birRate = 0
        self.evo = 40
        self.exp = exp
        self.tier = 1
        self.amount = amount 

   
class Skeleton(Zombie):
    def __init__(self, exp = 0, amount = 1):
        self.name = "Skeleton" 
        self.hp = 80
        self.atk = 5
        self.defense = 6
        self.atkSpd = 1.75
        self.intel = .1
        self.evo = 80
        self.exp = exp
        self.tier = 2
        self.amount = amount 

class SkeleAcol(Zombie):
    def __init__(self, exp = 0, amount = 1):
        self.name = "Skeleton Acolyte" 
        self.hp = 120
        self.atk = 8.5
        self.defense = 8
        self.atkSpd = 1.75
        self.intel = .1
        self.evo = 200
        self.exp = exp
        self.tier = 3
        self.amount = amount 

class SkeleMage(Zombie):
    def __init__(self, exp = 0, amount = 1):
        self.name = "Skeleton Mage" 
        self.hp = 150
        self.atk = 12
        self.defense = 10
        self.atkSpd = 1.75
        self.intel = .4
        self.evo = 1500
        self.exp = exp
        self.tier = 4
        self.amount = amount 

class Lich(Zombie):
    def __init__(self, exp = 0, amount = 1):
        self.name = "Lich" 
        self.hp = 300
        self.atk = 19
        self.defense = 16
        self.atkSpd = 2
        self.intel = .75
        self.exp = exp
        self.tier = 5
        self.amount = amount 