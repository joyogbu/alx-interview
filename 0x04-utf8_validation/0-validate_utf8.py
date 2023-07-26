#!/usr/bin/python3
'''utf-8 validation'''


import math


def validUTF8(data):
    '''defining the function'''
    # lis = []
    if not isinstance(data, list):
        return False
    lis2 = []
    lis3 = []
    for x in data:
        if x == 0:
            lis.append(0)
            # return False
        if x < 0:
            return False
        if type(x) is not int:
            return False
        lis = []
        while x > 0:
            res = x % 2
            lis.append(res)
            x = math.floor(x / 2)
            if x < 0:
                break
            lis2 = lis[::-1]
            if len(lis2) > 8:
                lis2.pop(0)
            lis4 = []
            if len(lis2) < 8:
                rem = 8 - len(lis2)
                for i in range(rem):
                    lis4.append(0)
                # lis2.append(0)
            lis4.extend(lis2)
        lis3.append(lis4)
        # lis2[:0] = [1]
    # print(lis3)
    no = 0
    for list_item in lis3:
        # print (list_item.index(0))
        if no == 0:
            if (list_item.index(0)) == 0:
                # no = 1
                continue
            elif (list_item.index(0)) == 2:
                no = 1
            elif (list_item.index(0)) == 3:
                no = 2
            elif (list_item.index(0)) == 4:
                no = 3
            else:
                return False
        else:
            if (list_item.index(0)) != 1:
                return False
            no -= 1
    return no == 0
