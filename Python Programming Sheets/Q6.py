askAnimal = True
while(askAnimal==True):
    answer = input("Type The Name Of An Animal")
    answer = answer.lower
    if(answer=="dog"):
        print("Dog goes Woof")
    elif(answer=="cat"):
        print("Cat goes Meow")
    elif(answer=="cow"):
        print("Cow goes Moo")
    elif(answer=="pig"):
        print("Pig goes Oink")
    elif(answer=="exit"):
        print("Exiting...")
        askAnimal = False
    else:
        print("Animal not recognised!")
