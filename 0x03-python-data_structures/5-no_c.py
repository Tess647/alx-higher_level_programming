#!/usr/bin/python3

def no_c(my_string):
    updatedStr = ''
    for i in my_string:
        if i != 'c' and i != 'C':
            updatedStr += i
        return updatedStr
