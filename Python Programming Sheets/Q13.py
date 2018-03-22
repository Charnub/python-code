import random
character = (input("Do you want to create a Character?"))
character = character.lower()
dice1 = random.randint(1,6)
dice2 = random.randint(1,12)
if character == "yes":
    calculate = dice2/dice1+10
    print("Hit Points: "+(str(calculate)))
elif character == "no":
    exit()
