filename = (input("Enter Filename: "))
message = (input("Enter Message: "))

f = open(filename+".txt", 'w')
f.write(message)
f.write("\n END MESSAGE")
f.close
