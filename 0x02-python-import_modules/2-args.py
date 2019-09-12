#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    if len(argv) == 1:
        print("0 arguments.")
    elif len(argv) > 1:
        if len(argv) == 2:
            print("{:d} argument:".format(len(argv) - 1))
            print("{:d}: {:s}".format(len(argv) - 1, argv[1]))
        else:
            print('{} arguments:'.format(len(argv) - 1))
            for a in range(1, len(argv)):
                print('{:d}: {:s}'.format(a, argv[a]))
