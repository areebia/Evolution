#Parent class for all races.


class Race:
    def __init__(self, name, hp, atk, defense, atkSpd, intel, amount, birRate, exp):
        self.name = name
        self.hp = hp
        self.atk = atk
        self.defense = defense
        self.atkSpd = atkSpd
        self.intel = intel
        self.amount = amount
        self.birRate = birRate
        self.exp = exp