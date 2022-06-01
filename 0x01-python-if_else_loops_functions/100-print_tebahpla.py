#!/usr/bin/python3
for alpha in reversed(range(97, 123)):
    if (alpha % 2 == 0):
        print("{:c}".format(alpha), end='')
    else:
        print("{:c}".format(alpha - 32), end='')
