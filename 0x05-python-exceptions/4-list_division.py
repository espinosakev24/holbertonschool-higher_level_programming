#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new = []
    for a in range(list_length):
        num = 0
        try:
            num = my_list_1[a] / my_list_2[a]
        except ZeroDivisionError:
            print('{:s}'.format('division by 0'))
        except TypeError:
            print('{:s}'.format('wrong type'))
        except IndexError:
            print('{:s}'.format('out of range'))
        finally:
            new.append(num)
    return new
