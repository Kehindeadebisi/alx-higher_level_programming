#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) is not str or roman_string is None:
        return 0
    roman_dict = {"I": 1, "V": 5, "X": 10, "L": 50,
                  "C": 100, "D": 500, "M": 1000}
    rev = roman_string[::-1]
    number = roman_dict[rev[0]]

    for i in range(len(rev) - 1):
        a = roman_dict[rev[i]]
        b = roman_dict[rev[i + 1]]
        if b >= a:
            number += b
        else:
            number -= before
    return number
