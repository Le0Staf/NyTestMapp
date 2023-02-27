import random 

n = random.randint(1,10)
gissning = int(input("Gissa ett nummer mellan 1 och 10: "))

while gissning != n:
    if gissning < n:
        print("För låg")
        gissning = int(input("Gissa igen: "))
    elif gissning == n: 
        print("För hög")
        gissning = int(input("Gissa igen: "))
    else:
        break
print("Du gissade rätt!")
