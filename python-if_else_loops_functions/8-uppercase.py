#!/usr/bin/python3
def uppercase(c):
    for letter in c:
        letter_ascii = ord(letter)
        if 97 <= letter_ascii <= 122:
            letter_ascii -= 32
        print("{}".format(chr(letter_ascii)), end="")
    print("\n", end="")
