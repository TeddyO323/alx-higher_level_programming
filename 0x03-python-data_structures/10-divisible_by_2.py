#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    listResult = []
    for number in my_list:
        if (number % 2 == 0):
            listResult.append(True)
        else:
            listResult.append(False)
    return listResult
