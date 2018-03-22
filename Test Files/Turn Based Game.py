import random, time
sEnemies = ("Giant", "Ogre", "Squirrel")
sEnemies2 = random.choice(sEnemies)
print("Turn Based Game (Charlie Parsons)")
print("-" * 40)
print("\033[0;31;0m A wild "+sEnemies2+" approaches!") # Sets the colour to red for that line
time.sleep(1)
print("\033[0;0;0m Your Health: 100") # Sets the colour back to black
print(" "+sEnemies2+"'s Health: 100")
iEnemyHealth = 100
iPlayerHealth = 100
print("-" * 40)
items = ("Sword", "Bow", "Arrows", "Health Potions")
iarrows = random.randint(2,4)
ihealthpot = random.randint(2,3)

bothAlive = True
time.sleep(2)
print("You have the following items available:")
print(items[0])
print(items[1]+" with"+" "+(str(iarrows))+" "+items[2])
print((str(ihealthpot))+" "+items[3])
print("-" * 40)

while iPlayerHealth > 0 and (bothAlive):
    sword = random.randint(5,20)
    bow = random.randint(10,30)
    healthpot = random.randint(10,20)
    enemyAttack = random.randint(10, 25)
    attack = (int(input("What would you like to do? Press 1 to attack with Sword. Press 2 to attack with Bow. Press 3 to use a Health Potion")))
    if attack == 1:
        iEnemyHealth = iEnemyHealth - sword
        print("\033[0;34;0m Swoosh")
        iPlayerHealth = iPlayerHealth - enemyAttack
        time.sleep(1)
        print("\033[0;31;0m You did "+(str(sword))+" damage to the "+sEnemies2)
        print("\033[0;0;0m The "+sEnemies2+" now has "+(str(iEnemyHealth))+" health remaining!")
        time.sleep(2)
        print("\033[0;34;0m Ouch! the "+sEnemies2+" hit you for "+(str(enemyAttack))+" damage!")
        print("\033[0;0;0m You now have "+(str(iPlayerHealth))+" health remaining!")
        if iEnemyHealth <= 0:
            bothAlive = False
            print("With one final swoosh of the sword the "+sEnemies2+" came crashing down!")
            print("Congratulations! You Win!!")
        if iPlayerHealth <= 0:
            bothAlive = False
            print("With one big swipe the " + sEnemies2 + " crushed and killed you")
            print("Sadly! You Lose!")
            print("Game Over!")
    elif attack == 2:
        if iarrows > 0:
            iEnemyHealth = iEnemyHealth - bow
            print("\033[0;34;0m Twang")
            iPlayerHealth = iPlayerHealth - enemyAttack
            iarrows -= 1
            print("\033[0;31;0m You did "+(str(sword))+" damage to the "+sEnemies2)
            print("\033[0;0;0m The " + sEnemies2 + " now has " + (str(iEnemyHealth)) + " health remaining!")
            time.sleep(2)
            print("\033[0;34;0m Ouch! the " + sEnemies2 + " hit you for " + (str(enemyAttack)) + " damage!")
            print("\033[0;0;0m You now have " + (str(iPlayerHealth)) + " health remaining!")
            if iEnemyHealth <= 0:
                bothAlive = False
                print("With one final twang of the bow the " + sEnemies2 + " came crashing down!")
                print("Congratulations! You Win!!")
            if iPlayerHealth <= 0:
                bothAlive = False
                print("With one big swipe the " + sEnemies2 + " crushed and killed you")
                print("Sadly! You Lose!")
                print("Game Over!")
        else:
            print("You have no arrows remaining!")
    elif attack == 3:
        if ihealthpot > 0:
            iPlayerHealth = iPlayerHealth + healthpot
            ihealthpot -=1
            print("\033[0;34;0m You have been healed by "+(str(healthpot))+" health!")
            print("\033[0;0;0m You now have "+(str(iPlayerHealth))+" health remaining!")
            if iPlayerHealth <= 0:
                bothAlive = False
                print("With one big swipe the " + sEnemies2 + " crushed and killed you")
                print("Sadly! You Lose!")
                print("Game Over!")
        else:
            print("You have no Health Potions remaining!")


