#!/usr/bin/python3

for alphaLetters in range(97, 123):
    if alphaLetters == 113 or alphaLetters == 101:
        continue
    else:
        print("{:c}".format(alphaLetters), end="")
