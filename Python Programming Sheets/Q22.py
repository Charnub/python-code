myMessage = (input("Enter Message: "))
upperLower = (input("Shout or Whisper?: "))
upperLower = upperLower.lower()
if upperLower == "shout":
    myShout = myMessage.upper()
    print(myShout)
elif upperLower == "whisper":
    myShout2 = myMessage.lower()
    print(myShout2)
