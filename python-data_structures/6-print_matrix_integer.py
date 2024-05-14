#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    if matrix:
        for row in matrix:
            for number in row:
                print("{:d}".format(number), end=" ")
            print()
