#Parent class for all races.


class Race:
    def __init__(self, name=0, hp=0, atk=0, defense=0, atkSpd=0, intel=0, amount=1, birRate=0, exp=0, evo=0, tier=1):
        self.name = name
        self.hp = hp
        self.atk = atk
        self.defense = defense
        self.atkSpd = atkSpd
        self.intel = intel
        self.amount = amount
        self.birRate = birRate
        self.exp = exp
        self.evo = evo
        self.tier = tier

    def evolve(self):
        if self.exp > self.evo:
            return True
        return False



def main():
    print("begin")   
    x = Race(exp = 5, evo= 1)

    print(x.tier) 
    if x.evolve() == True:
        print(x.exp, " is greater than ", x.evo, ", therefore evolve")
    elif x.evolve() == False:   
        print(x.exp, " is less than ", x.evo, ", therefore no evolve")
    else:
        print("dis no werk")

if __name__ == '__main__':
    main()