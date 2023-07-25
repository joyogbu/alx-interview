#!/usr/bin/python3
'''utf-8 validation'''


import math


def validUTF8(data):
    '''defining the function'''
    # lis = []
    lis2 = []
    lis3 = []
    for x in data:
        lis = []
        while x > 0:
            res = x % 2
            lis.append(res)
            x = math.floor(x / 2)
            if x < 0:
                break
            lis2 = lis[::-1]
            lis4 = []
            if len(lis2) < 8:
                rem = 8 - len(lis2)
                for i in range(rem):
                    lis4.append(0)
                # lis2.append(0)
            lis4.extend(lis2)
    # print(lis4)
        lis3.append(lis4)
        # lis2[:0] = [1]
    # print(lis3)
    no = 0
    for list_item in lis3:
        # print (list_item.index(0))
        if (list_item.index(0)) == 0:
            continue
        elif (list_item.index(0)) == 2:
            no = 2
        elif (list_item.index(0)) == 3:
            no = 3
        elif (last_item.index(0)) == 4:
            no = 4
        else:
            return False
    return True
