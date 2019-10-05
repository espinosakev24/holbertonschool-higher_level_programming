#!/usr/bin/python3
"""
    module
    com 1
    com 2
"""


def text_indentation(text):
    """
    function that change char for breakline
    """
    s1 = text.replace('.', '.\n\n')
    s2 = s1.replace('?', '?\n\n')
    s3 = s2.replace(':', ':\n\n')
    new = s3.split('\n\n')
    if len(new[-1]) == 0:
        del new[-1]
    for i in new:
        print(i.lstrip(), end="")
        if i == new[-1] and i != ':' and i != '.' and i != '?':
            break
        print('\n')
