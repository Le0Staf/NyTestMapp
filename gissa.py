import random 

n = random.randrange(1,10)
gissning = int(input("Gissa ett nummer mellan 1 och 10: "))
gissningar = 2

while gissning != n:
    if gissningar > 0 and gissning < n:
        print(n)
        print("För låg")
        gissningar = gissningar - 1
        gissning = int(input("Gissa igen: "))
    elif gissningar >0 and gissning > n: 
        print(n)
        print("För hög")
        gissningar = gissningar - 1
        gissning = int(input("Gissa igen: "))
    elif gissning <= 0:
        print("Slut Med Gissningar")
        break
else:
    print("Du Gissade Rätt!")
        
