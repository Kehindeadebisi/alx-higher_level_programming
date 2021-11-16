#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if number >+ 0:
    last = number % 10
elif number < 0:
    last = ((number * -1) % 10) * -1

ist = "Last digit of"
if last < 6 and last != 0:
    print("{} {} is {} and is less than 6 and not 0".format(ist, number, last))
elif last == 0:
    print("{} {} is {} and is 0".format(ist, number, last))
elif last > 5:
    print("{} {} is {} and is greater than 5".format(ist, number, last))
