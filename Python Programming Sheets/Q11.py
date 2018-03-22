import random
diceRoll = True
while diceRoll == True:
    roll = (input("Would you like to roll the dice 100 times or exit?"))
    roll = roll.lower()
    if roll == "roll":
        for i in range(1,100):
            dice = random.randint(1,6)
            print(dice)
    elif roll == "exit":
        diceRoll = False
