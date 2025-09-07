def collatz(number):
    while number != 1:
        if (number % 2) == 0:
            number = number // 2
            print(number, sep='')
        elif number % 2 == 1:
            number = 3 * number + 1
            print(number)
    return number

try:
    number = int(input("please enter a number: "))
    collatz(number)
except ValueError:
    print('please enter a number, not letter')