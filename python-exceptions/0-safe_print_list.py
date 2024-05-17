#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    nbrPrinted = 0
    try:
        for nbrPrinted in range(x):
            print(my_list[nbrPrinted], end="")
            nbrPrinted += 1
    except IndexError:
        pass
    print()
    return (nbrPrinted)
