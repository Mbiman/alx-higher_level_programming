#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv
    number = len(argv)
    add = 0
    for i in range(1, number):
        add += int(argv[i])
    print("{}".format(add))
    