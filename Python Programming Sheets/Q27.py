def coinToss():
    import random
    if(random.randint(0,1)==0):
        return "Heads"
    else:
        return "Tails"
print(coinToss())