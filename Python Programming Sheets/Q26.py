def makeRandomDice(sides):
    import random
    roll = random.randint(1, sides)
    print("You rolled a", roll)

for i in range(1,213):
    makeRandomDice(6)
    