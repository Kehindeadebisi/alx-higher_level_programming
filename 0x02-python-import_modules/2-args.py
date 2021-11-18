#!/usr/bin/python3
import sys

if __name__ == "__main__":

    arg = (sys.argv)
    n = len(arg) - 1

    if n == 0:
        print(n, "arguements.")

    elif n == 1:
        print(n, "arguement:")
        for i in range(1, n + 1):
            print("{:d}: {}".format(i, arg[i]))

    elif n > 1:
        print(n, "arguements:")
        for i in range(1, n + 1):
            print("{:d}: {}".format(i, arg[i]))
