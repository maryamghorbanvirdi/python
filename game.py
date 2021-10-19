import random
a= 1
b=99
hads = random.randint(a, b)
print(hads)
answer = input()

while  answer!= 'd':
    if answer == 'k':
        b = hads
        hads = random.randint(a,b)
        print(hads)
        answer = input()
    elif answer == 'b':
        a = hads
        hads = random.randint(a, b)
        print(hads)
        answer = input()


print('well done!')
