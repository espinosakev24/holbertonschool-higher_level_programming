#!/usr/bin/python3
"""Module of """


class MyList(list):
    """Function MyList"""

    def print_sorted(self):
        new = self.copy()
        new.sort()
        print(new)
