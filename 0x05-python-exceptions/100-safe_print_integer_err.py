#!/usr/bin/python3
def safe_print_integer_err(value):
    try:
        print('{:d}'.format(value))
    except Exception as a:
        eprint('Exception: {}'.format(a))
        return False
    return True
