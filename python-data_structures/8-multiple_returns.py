#!/usr/bin/python3

def multiple_returns(sentence):
    length_string = len(sentence)
    if length_string != 0:
        first_char = sentence[0]
    else:
        first_char = None
    return (length_string, first_char)
