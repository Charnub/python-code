aPack = []
aValue = []
aPosition = []
sSuits = ["Diamonds", "Hearts", "Spades", "Clubs"]
sNumbers = ["Ace", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King"]
for a in range (0,52):
    nPosition = []
    aPack.append(nPosition)
    aPack[a].append(a)
for b in range (0,11):
    nPosition2 = []
    aValue.append(nPosition2)
    aValue[b].append(b)
for c in range (0,13):
    nPosition3 = []
    aPosition.append(nPosition3)
    aPosition[c].append(c)
for d in range (0,13):
    aNewPack = []
    aNewPack.append(d)
    Diamonds = (sNumbers[d], "of", sSuits[0])
    Hearts = (sNumbers[d], "of", sSuits[1])
    Spades = (sNumbers[d], "of", sSuits[2])
    Clubs = (sNumbers[d], "of", sSuits[3])
    print(Clubs)
    print(Diamonds)
    print(Spades)
    print(Hearts)
print(aPack)
print(aValue)
print(aPosition)

