#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    a = 0
    b = 0
    for i in range(len(tuple_a)):
        if (i == 0):
            a += tuple_a[i]
        if (i == 1):
            b += tuple_a[i]
    for i in range(len(tuple_b)):
        if (i == 0):
            a += tuple_b[i]
        if (i == 1):
            b += tuple_b[i]
    newTuple = a, b
    return newTuple
