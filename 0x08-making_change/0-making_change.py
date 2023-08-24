#!/usr/bin/python3
'''Find minimum number of coins that make a given value'''


import sys


def makeChange(coins, total):
    '''change coins from within'''
    if total <= 0:
        return 0
    length = len(coins)
    res = sys.maxsize
    for i in range(0, length):
        if coins[i] <= total:
            sub_res = makeChange(coins, total - coins[i])
            if (sub_res != sys.maxsize and sub_res + 1 < res):
                res = sub_res + 1
    return res
