#!/usr/bin/python3
def remove_char_at(str, n):
    i = 0
    str2 = ""
    for char in str[:]:
        if i != n:
            str2 += char
        i += 1
    return str2
