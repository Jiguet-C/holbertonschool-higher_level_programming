#!/usr/bin/python3

def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return (0)

    roman_values = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
        }

    total = 0
    prev_value = 0

    for character in reversed(roman_string):
        if character in roman_values:
            current_value = roman_values[character]
            if current_value >= prev_value:
                total += current_value
            else:
                total -= current_value
            prev_value = current_value
        else:
            return (0)

    return (total)
