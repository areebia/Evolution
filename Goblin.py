import Race

class Goblin(Race.Race):
   
    def __init__(self, exp = 0):
        self.name = "Goblin" 
        self.hp = 10
        self.atk = 1
        self.defense = 1
        self.atkSpd = 3
        self.intel = .1
        self.birRate = .55
        self.exp = exp

   
class Hobgoblin(Goblin):
    def __init__(self, exp = 0):
        self.name = "Hobgoblin" 
        self.hp = 50
        self.atk = 5
        self.defense = 4
        self.atkSpd = 3
        self.intel = .2
        self.exp = exp

class GoblinChief(Goblin):
    def __init__(self, exp = 0):
        self.name = "Goblin Chief" 
        self.hp = 100
        self.atk = 7.5
        self.defense = 7
        self.atkSpd = 3
        self.intel = .2
        self.exp = exp

class GoblinLord(Goblin):
    def __init__(self, exp = 0):
        self.name = "Goblin Lord" 
        self.hp = 175
        self.atk = 10
        self.defense = 8
        self.atkSpd = 3
        self.intel = .4
        self.exp = exp

class GoblinKing(Goblin):
    def __init__(self, exp = 0):
        self.name = "Goblin King" 
        self.hp = 250
        self.atk = 15
        self.defense = 14
        self.atkSpd = 3
        self.intel = .55
        self.exp = exp