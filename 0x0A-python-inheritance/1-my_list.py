#!/usr/bin/python3
"""Module of my list"""


class MyList(list):
    """Function MyList"""

    def print_sorted(self):
        """
        Print sorted
        """
        new = self.copy()
        new.sort()
        print(new)
