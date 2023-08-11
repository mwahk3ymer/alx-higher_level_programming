#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    if 0 <= idx < len(my_list):
        my_list[idx] = element
    return my_list

my_list = [1, 2, 3, 4, 5]
replace_in_list(my_list, 2, 10)
print(my_list)
