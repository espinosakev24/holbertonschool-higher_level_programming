#!/usr/bin/python3
def safe_print_integer(value):
    try:
        print('{:d}'.format(value))
    except NameError:
        return False
    except ValueError:
        return False
    return True
