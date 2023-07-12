#!/usr/bin/python3
'''minimum operations required'''


def minOperations(n):
    '''defining the function'''
    char = 1
    op = 2
    if n <= 0:
        return (0)
    while char < n:
        op += 1
        if char == n:
            break
        char += 1
    return (op - (n//2 - 1))
