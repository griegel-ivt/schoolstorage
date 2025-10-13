#Array of 15 test numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

#For every list entry, if it is divisible by two, it is even, otherwise odd
for number in numbers:
    if (number % 2 == 0):
        print(str(number) + " is even")
    else:
        print(str(number) + " is odd")
