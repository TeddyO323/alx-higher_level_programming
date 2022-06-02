#!/usr/bin/python3
import sys

if __name__ == "__main__":
    sum = 0
    count = 0
    if len(sys.argv) >= 2:
        for i in sys.argv:
            if count >= 1:
                sum = sum + int(i)
            count += 1
        print("{:d}".format(sum))
    else:
        print("{:d}".format(len(sys.argv) - 1))
