listNames = []
myNames = ""
while(myNames!="stop"):
    myNames = input("Type a name, or stop: ")
    if(myNames!="stop"):
        listNames.append(myNames)

f = open("names.txt", 'w')
f.write(str(listNames))
f.close()