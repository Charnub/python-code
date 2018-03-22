sSentence = "Good Afternoon"
bFlipLetter = True
sNewSentence = ""
for i in range(0, len(sSentence)):
    if sSentence[i] == " ":
        bFlipLetter = False
    else:
        bFlipLetter = bFlipLetter

    if bFlipLetter == True:
        sLetter = sSentence[i].upper()
        bFlipLetter = not bFlipLetter
    else:
        sLetter =sSentence[i].lower()
        bFlipLetter = not bFlipLetter
    sNewSentence = sNewSentence + sLetter
print(sNewSentence)
