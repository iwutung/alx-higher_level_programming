#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sort = dict(sorted(a_dictionary.items()))
    for key, value in sort.items():
        print("{}: {}".format(key, value))
