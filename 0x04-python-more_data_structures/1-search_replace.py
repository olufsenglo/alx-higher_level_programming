#!/usr/bin/python3

def search_replace(my_list, search, replace):
    return([replace if search == i else i for i in my_list])

my_list = [1, 2, 3, 4, 5, 4, 2, 1, 1, 4, 89]
print(search_replace(my_list, 5, 111))
