#!/usr/bin/python3
def fizzbuzz():
    for i in range(1, 101):
        mot = i
        if (i % 3 == 0 and i % 5 == 0):
            mot = "FizzBuzz"
        elif (i % 3 == 0):
            mot = "Fizz"
        elif (i % 5 == 0):
            mot = "Buzz"
        print("{}".format(mot), end=' ')
