#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    division = []
    for element in range(list_length):
        try:
            division.append(my_list_1[element] / my_list_2[element])
        except ZeroDivisionError:
            print("division by 0")
            division.append(0)
        except TypeError:
            print("wrong type")
            division.append(0)
        except IndexError:
            print("out of range")
            division.append(0)
        finally:
            pass
    return (division)
