#!/usr/bin/python3
def safe_function(fct, *args):
    try:
        return fct(*args)
    except Exception as error:
        import sys
        sys.stderr.write('Exception: {}\n'.format(error))
