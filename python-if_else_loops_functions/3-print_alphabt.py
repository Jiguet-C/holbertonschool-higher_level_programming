#!/usr/bin/python3
for letter in range(97, 123):
    if letter != 113 and letter != 101:
        print("{:s}".format(chr(letter)), end="")
