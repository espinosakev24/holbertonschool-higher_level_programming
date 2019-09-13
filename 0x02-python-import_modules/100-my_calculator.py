#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    from calculator_1 import add, sub, mul, div
    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    s1 = argv[1]
    s2 = argv[2]
    s3 = argv[3]
    if argv[2] == '+' or argv[2] == '-' or argv[2] == '*' or argv[2] == '/':
        if argv[2] == '+':
            print('{} {} {} = {:d}'.format(s1, s2, s3, add(int(s1), int(s3))))
        if argv[2] == '-':
            print('{} {} {} = {:d}'.format(s1, s2, s3, sub(int(s1), int(s3))))
        if argv[2] == '*':
            print('{} {} {} = {:d}'.format(s1, s2, s3, mul(int(s1), int(s3))))
        if argv[2] == '/':
            print('{} {} {} = {:d}'.format(s1, s2, s3, div(int(s1), int(s3))))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
