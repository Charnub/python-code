file = open("Fruits.txt", 'r')
Fruit = input("Enter a name of a fruit: ")
dFruit = {file.read()}
print(dFruit[Fruit])
sAddFruit = input("What fruit would you like to add?: ")
sAddFruitNum = input("How many "+sAddFruit+"'s are there?: ")
dFruit[sAddFruit] = sAddFruitNum
print(dFruit)

