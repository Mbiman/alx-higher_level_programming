#!/usr/bin/python3

def no_c(my_string):
    chars = 'cC'
    for c in chars:
        my_string = my_string.replace(c, '')
    
    return my_string
