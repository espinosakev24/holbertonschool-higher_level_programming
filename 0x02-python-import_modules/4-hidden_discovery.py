#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    str = dir(hidden_4)
    for a in str:
        if a[0] != '_':
            print(a)
