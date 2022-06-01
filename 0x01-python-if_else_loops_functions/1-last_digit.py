#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if number < 0:
    lastDig = (number * -1) % 10
    lastDig *= -1
else:
    lastDig = number % 10

if (lastDig > 5):
    print("Last digit of {:d} is {:d} and is greater than 5".format(number,
                                                                    lastDig))
elif (lastDig == 0):
    print("Last digit of {:d} is {:d} and is 0".format(number, lastDig))
else:
    print("Last digit of {:d} is {:d} and is less than 6 and not 0".format
          (number, lastDig))
