#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    import calculator_1
if (len(sys.argv) == 4):
    operator = sys.argv[2]
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    if(operator == "+"):
        print("{} + {} = {}".format(a, b, calculator_1.add(a, b)))
    elif(operator == "-"):
        print("{} - {} = {}".format(a, b, calculator_1.sub(a, b)))
    elif(operator == "*"):
        print("{} * {} = {}".format(a, b, calculator_1.mul(a, b)))
    elif(operator == "/"):
        print("{} / {} = {}".format(a, b, calculator_1.div(a, b)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
else:
    print("Usage: ./100-my_calculator.py <a> <operator> <b>")
    exit(1)
