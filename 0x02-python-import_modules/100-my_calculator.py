#!/usr/bin/python3
if __name == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div

    arg_vec = sys.argv
    arg_cnt = len(argv) - 1

    if arg_cnt != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    a = int(argv[1])
    b = int(argv[3])
    operator = int(argv[2])
    ans = 0

    if operator == "+":
        ans = add(a, b)
    elif operator == "-":
        ans = sub(a, b)
    elif operator == "*":
        ans = mul(a, b)
    elif operator == "/":
        ans = div(a, b)
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    print("{:d} {} {:d} = {:d}".format(a, operator, b, ans))
