#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    print('{:d} arguments'.format(len(argv)))
    for a in range(1, len(argv)):
        print('{:d}: {:s}'.format(a, argv[a]))
