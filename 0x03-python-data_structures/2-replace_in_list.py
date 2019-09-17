def replace_in_list(my_list, idx, element):
    a = 0
    if not(idx < 0 or idx > len(my_list)):
        for n in my_list:
            if idx == a:
                my_list[a] = element
                return my_list
            a += 1
my_list = [1, 2, 3, 4, 5]
idx = 3
new_element = 9
new_list = replace_in_list(my_list, idx, new_element)

print(new_list)
print(my_list)
