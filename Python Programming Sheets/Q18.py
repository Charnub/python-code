filename = (input("Enter Filename: "))
f = open("C:\\Users\\Charn\\Documents\\Computing\\All Code\\"+filename+".txt", 'r')
file1 = f.readlines()
f.close()

print(file1)