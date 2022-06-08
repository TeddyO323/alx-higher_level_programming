#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    else:
        up = 0
        down = 0
        for values in my_list:
            up += values[0] * values[1]
            down += values[1]
        result = up / down
    return result
