win = 0
sum = 0
for i in range(1, 31):
    a = int(input('please enter your number: '))
    sum = sum + a
    if a == 3:
        win = win +1

print(sum,'',win)


