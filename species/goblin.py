import Race

class Goblin(Race.Race):
   
    def __init__(self, exp = 0, amount = 1):
        self.name = "Goblin" 
        self.hp = 10
        self.atk = 1
        self.defense = 1
        self.atkSpd = 3
        self.intel = .1
        self.birRate = .55
        self.evo = 20
        self.exp = exp
        self.tier = 1
        self.amount = amount
        

   
class Hobgoblin(Goblin):
    def __init__(self, exp = 0, amount = 1):
        self.name = "Hobgoblin" 
        self.hp = 50
        self.atk = 5
        self.defense = 4
        self.atkSpd = 3
        self.intel = .2
        self.evo = 50
        self.exp = exp
        self.tier = 2
        self.amount = amount

class GoblinChief(Goblin):
    def __init__(self, exp = 0, amount = 1):
        self.name = "Goblin Chief" 
        self.hp = 100
        self.atk = 7.5
        self.defense = 7
        self.atkSpd = 3
        self.intel = .2
        self.evo = 500
        self.exp = exp
        self.tier = 3
        self.amount = amount

class GoblinLord(Goblin):
    def __init__(self, exp = 0, amount = 1):
        self.name = "Goblin Lord" 
        self.hp = 175
        self.atk = 10
        self.defense = 8
        self.atkSpd = 3
        self.intel = .4
        self.evo = 2000
        self.exp = exp
        self.tier = 4
        self.amount = amount

class GoblinKing(Goblin):
    def __init__(self, exp = 0, amount = 1):
        self.name = "Goblin King" 
        self.hp = 250
        self.atk = 15
        self.defense = 14
        self.atkSpd = 3
        self.intel = .55
        self.exp = exp
        self.tier = 5 
        self.amount = amount





def main():
    x = Goblin() 
    x.exp = 25
    print(x.evo, x.tier)
    x.amount = 10
    print("amount:", x.amount)
    if x.evolve() == True:
        print(x.exp, " is greater than ", x.evo, ", therefore evolve")
        y = Hobgoblin(exp= x.exp-x.evo) 
    elif x.evolve() == False:   
        print(x.exp, " is less than ", x.evo, ", therefore no evolve")
    else:
        print("dis no werk")
    
    print("exp:", y.exp, " name:", y.name, " atk:", y.atk, " tier:", y.tier, " amount:", y.amount)

if __name__ == '__main__':
    main()