run = True
while run == True:
    askUser = (input("Open, Create or Exit?: "))
    askUser = askUser.lower()
    if askUser == "create":
        filename = (input("Enter Filename: "))
        enterText = (input("Enter Text: "))
        f = open(filename+".txt", 'w')
        f.write(enterText)
        f.close
    elif askUser == "open":
        filename2 = (input("Enter Filename: "))
        f = open("C:\\Users\\Charn\\Documents\\Computing\\All Code\\"+filename2+".txt", 'r')
        fileText = f.readline()
        f.close()
        print(fileText)
    elif askUser == "exit":
        run = False



