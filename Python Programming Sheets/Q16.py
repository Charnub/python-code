import random
play = True
while play == True:
    play2 = (input("Would you like to play or exit?"))
    play2 = play2.lower()
    if play2 == "play":
        attempts = 0
        numberGuess = True
        number = random.randint(1,100)
        while numberGuess == True:
            userGuess = (int(input("Guess the number: ")))
            if userGuess < number:
                print("Too Low!")
                attempts += 1
            elif userGuess > number:
                print("Too High!")
                attempts += 1
            elif userGuess == number:
                print("Correct!")
                print("Attempts taken: "+(str(attempts)))
                numberGuess = False
    elif play2 == "exit":
        play = False