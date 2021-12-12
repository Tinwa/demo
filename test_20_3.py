#!/usr/bin/python3
def multi(*n):
    result = 1
    count = 0
    try:
        for i in n:
            count += 1
            i = i + 1 - 1
            result *= i
    except TypeError:
        return('Invalid arg %d'%count)
    return result
print(eval(input()))