#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    from calculator_1 import add, sub, mul, div
    if len(argv) < 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    if argv[2] == '+':
        print('{}'.format(add(int(argv[1]), int(argv[3]))))
    if argv[2] == '-':
        print('{}'.format(sub(int(argv[1]), int(argv[3]))))
    if argv[2] == chr(42):
        print('{}'.format(mul(int(argv[1]), int(argv[3]))))
    if argv[2] == '/':
        print('{}'.format(div(int(argv[1]), int(argv[3]))))
