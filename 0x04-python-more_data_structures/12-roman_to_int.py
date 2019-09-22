#!/usr/bin/python3
def roman_to_int(roman_string):
    idx = 0
    r = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    it = 0
    res = 0
    if not (roman_string) or roman_string == None:
        return 0
    for num in range(len(roman_string)):
        if r[roman_string[num - 1]] > r[roman_string[num]]:
            res -= r[roman_string[num]]
        else:
            res += r[roman_string[num]]
    return res

roman_number = "X"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "VII"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "IX"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "LXXXVII"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "DCCVII"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))
roman_number = "IV"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))
roman_number = "V"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))
