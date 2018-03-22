def Kaprekar(n):
    if n == '1':
        return True
    sq = ((int(n)**2))
    for i in range(1,len(sq)):
        if (int(sq[:i]) + int(sq[i:]) == int(n)) and (int(sq[:i]) > 0) and (int(sq[i:])>0):
            return True
    return False
def Find(m, n):
    return [(i) for i in range(m,n+1) if Kaprekar((i))]
 
m = int(input('Where to start?\n'))
n = int(input('Where to stop?\n'))
KNumbers = Find(m, n,)
for i in KNumbers:
    print(i)
print('The number of Kaprekar Numbers found are'),
print(len(KNumbers))
input()