number = int(input('enter a number: '))

sum = 0
count = 0
average = 0

while number != -1:
    number = int(input('enter a number: '))
    sum = sum + number
    count = count +1
    average = sum/count
    print(sum)
    print(count)
    print(average)
    print(sum, count, average)
    if number == -1:
        print(sum, count, average)
        break
        

