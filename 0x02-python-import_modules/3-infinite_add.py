#!/usr/bin/python3
import sys
if __name__ == "__main__":
    args = sys.argv
    n = len(args)

    for i in range(1, n):
        sum += int(args[i])

    print(sum)
