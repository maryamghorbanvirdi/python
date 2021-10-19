import random

a = int(input("enter a number: "))
i = random.randint(1, 99)
print(i)
while i != a:
    if a % i == 0:
        print("not prime")
    else :
        print("prime")
    break