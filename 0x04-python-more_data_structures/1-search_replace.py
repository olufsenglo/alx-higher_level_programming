#!/usr/bin/python3

def search_replace(my_list, search, replace):
    if not my_list:
        return my_list
    return([replace if search == i else i for i in my_list])
