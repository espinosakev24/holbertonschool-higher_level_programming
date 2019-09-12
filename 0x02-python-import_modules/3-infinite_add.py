#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    if len(argv) > 0:
        print(sum(map(int, argv[1:])))
