#!/usr/bin/python3
def safe_print_division(a, b):
    total = 0
    try:
        total = a / b
    except ZeroDivisionError:
        total = None
    finally:
        print('Inside result: {}'.format(total))
        return total
a = 12
b = 2
result = safe_print_division(a, b)
print("{:d} / {:d} = {}".format(a, b, result))

a = 12
b = 0
result = safe_print_division(a, b)
print("{:d} / {:d} = {}".format(a, b, result))
