#!/usr/bin/python3
'''Find minimum number of coins that make a given value'''


import sys


def makeChange(coins, total):
    '''change coins from within'''
    if total <= 0:
        return 0
    length = len(coins)
    res = [-sys.maxsize] * (total + 1)
    res[0] = 0
    for i in range(1, total + 1):
        for j in range(length):
            if coins[j] < i:
                sub_res = res[i - coins[j]]
                if (sub_res != -sys.maxsize and sub_res + 1 < res[i]):
                    res = sub_res + 1
    if res[total] == -sys.maxsize:
        return -1
    else:
        return res[total]
