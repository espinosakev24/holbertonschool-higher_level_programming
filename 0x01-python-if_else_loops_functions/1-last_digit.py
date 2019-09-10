#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number > 0:
    mod = number % 10
else:
    mod = number % -10
s = "Last digit of"
s2 = "and is less than 6 and not 0"
s3 = "and is greater than 5"
if mod > 5:
    print('{:s} {:d} is {:d} {:s}'.format(s, number, number % 10, s3))
elif mod == 0:
    print('{:s} {:d} is {:d} and is 0'.format(s, number, number % 10))
elif mod > 0 and mod < 6:
    print('{:s} {:d} is {:d} {:s}'.format(s, number, number % 10, s2))
elif mod < 0:
    print('{:s} {:d} is {:d} {:s}'.format(s, number, number % -10, s2))
