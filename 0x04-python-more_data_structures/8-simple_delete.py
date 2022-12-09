#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    a_dictionary.pop(key, None)
    #del  a_dictionary[key]
    return a_dictionary
