import Race

class Elf(Race.Race):
   
    def __init__(self, exp = 0, amount = 1):
        self.name = "Elf" 
        self.hp = 50
        self.atk = 2.5
        self.defense = 2.5
        self.atkSpd = 2.5
        self.intel = .5
        self.birRate = .2
        self.evo = 50
        self.exp = exp
        self.tier = 1
        self.amount = amount

   
class ElfScout(Elf):
    def __init__(self, exp = 0, amount = 1):
        self.name = "Elf Scout" 
        self.hp = 80
        self.atk = 6
        self.defense = 5
        self.atkSpd = 2.5
        self.intel = .55
        self.evo = 120
        self.exp = exp
        self.tier = 2
        self.amount = amount

class ElfRanger(Elf):
    def __init__(self, exp = 0, amount = 1):
        self.name = "Elf Ranger" 
        self.hp = 120
        self.atk = 10
        self.defense = 8
        self.atkSpd = 2.5
        self.intel = .6
        self.evo = 220
        self.exp = exp
        self.tier = 3
        self.amount = amount

class ElfArcher(Elf):
    def __init__(self, exp = 0, amount = 1):
        self.name = "Elf Archer" 
        self.hp = 150
        self.atk = 14
        self.defense = 10
        self.atkSpd = 2.5
        self.intel = .7
        self.evo = 1100
        self.exp = exp
        self.tier = 4
        self.amount = amount

class ElfSniper(Elf):
    def __init__(self, exp = 0, amount = 1):
        self.name = "Elf Sniper" 
        self.hp = 250
        self.atk = 19
        self.defense = 14
        self.atkSpd = 2.75
        self.intel = .8
        self.exp = exp
        self.tier = 5
        self.amount = amount