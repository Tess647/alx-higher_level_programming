#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    result = []

    for num in range(len(my_list)):
        if my_list[num] % 2 == 0:
            result.append(True)
        else:
            result.append(False)
    return result
