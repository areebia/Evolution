#inherent bias in code, variables ending in 
#1 should be part of race with higher atk spd


def combat(racelist1, racelist2):
    #first list of race stats added together
    hp1 = sum([obj.hp for obj in racelist1])
    atk1 = sum([obj.atk for obj in racelist1])
    def1 = sum([obj.defense for obj in racelist1])
    

    #second list of opposing race stats added together
    hp2 = sum([obj.hp for obj in racelist2])
    atk2 = sum([obj.atk for obj in racelist2])
    def2 = sum([obj.defense for obj in racelist2])
    

    dead = False
    counter = 1
    while dead:
        hp1 -= calcDamage(def1, atk2)
        hp2 -= calcDamage(def2, atk1)
        if extraAtk(racelist1[0].atkspd, racelist2[0].atkSpd, counter):
           hp2 -= calcDamage(def2, atk1)

        counter += 1
    


#always input larger atkspd first 
def extraAtk(as1, as2, counter):
    if as1 > as2:
        dv = as1 - int(as2)  #math.modf(as1/as2)
        if dv * counter % (1/dv) == 0:
            return True 
    return False

        
    

#shaves off percentage of the total atk damage of enemy
def calcDamage(defense, attack):
    dmgPercent = 10 / (10 + defense)
    atkDmg = attack * (1 - dmgPercent)
    return atkDmg