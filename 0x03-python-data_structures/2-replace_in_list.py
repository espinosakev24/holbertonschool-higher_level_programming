#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
	a = 0
	if idx < 0 or idx > len(my_list):
		return my_list
	else:
		for n in my_list:
			if idx == a:
				my_list[a] = element
				return my_list
			a += 1
