#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    total_arg = len(argv)

    if total_arg - 1 == 0:
        print("{} arguments.\n".format(total_arg - 1), end="")
    elif total_arg - 1 == 1:
        print("{} argument:\n".format(total_arg - 1), end="")
    else:
        print("{} arguments:\n".format(total_arg - 1), end="")

    if total_arg != 0:
        for index in range(1, total_arg):
            print("{}: {}".format(index, argv[index]))
