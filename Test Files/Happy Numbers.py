def ishappy(n):
    cache = []
    while n != 1:
        n = sum(int(i)**2 for i in str(n))
        if n in cache:
            return False
        cache.append(n)
    return True
    
happies = []

for i in range(1, 1001):
    if ishappy(i): happies.append(i)
    

print("Happy numbers:")
print(happies)
