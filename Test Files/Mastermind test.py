aSequence = ["re","gr","bl","ye"]
aGuess = ["re","bl","gr","bk"]
def ColourPos():
    nColours = 0
    nPosition = 0
    for a in range (0,4):
        if aGuess[a] == aSequence[a]:
            nPosition +=1
        for b in range (0,4):
            if aGuess[a] == aSequence[b]:
                nColours +=1
def Mastermind():
    print("Welcome please give me 4 colours!")
    print("re for Red")
    print("bl for Blue")
    print("or for Orange")
    print("bk for Black")
    print("gr for Green")
    print("ye for Yellow")
    print("gy for Grey")

    ColourPos()

    print("Correct colours: "+(str(nColours)))
    print("Colours in correct positions: "+(str(nPosition)))


Mastermind()
