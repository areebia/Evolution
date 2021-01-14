import  species


def main():
    x = species.Race()
    x.exp = 25
    print(x.evo, x.tier)
    x.amount = 10
    print("amount:", x.amount)
    if x.evolve() == True:
        print(x.exp, " is greater than ", x.evo, ", therefore evolve")
        y = races.Race(exp= x.exp-x.evo) 
    elif x.evolve() == False:   
        print(x.exp, " is less than ", x.evo, ", therefore no evolve")
    else:
        print("dis no werk")
    
    print("exp:", y.exp, " name:", y.name, " atk:", y.atk, " tier:", y.tier, " amount:", y.amount)

if __name__ == '__main__':
    main()