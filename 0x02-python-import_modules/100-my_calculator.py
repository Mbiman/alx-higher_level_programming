#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv
    from calculator_1 import add, mul, sub, div

    number = len(argv)
    if number != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    else:
        a = int(argv[1])
        operator = str(argv[2])
        b = int(argv[3])
        if operator == '+':
            print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))
        elif operator == '-':
            print("{:d} - {:d} = {:d}".format(a, b, sub(a, b)))
        elif operator == '*':
            print("{:d} * {:d} = {:d}".format(a, b, mul(a, b)))
        elif operator == '/':
            print("{:d} / {:d} = {:d}".format(a, b, div(a, b)))
        else:
            print("{}".format(
                'Unknown operator.Available operators: +, -, * and /'))
            exit(1)
