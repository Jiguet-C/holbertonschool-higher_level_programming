#!/usr/bin/python3
import sys

if __name__ == "__main__":
    args = sys.argv[1:]
    addition = sum(int(numbers) for numbers in args)
    print(addition)
