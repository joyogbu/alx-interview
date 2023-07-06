#!/usr/bin/python3
'''lockboxes implementation'''


def canUnlockAll(boxes):
    '''defining the function'''
    for box in boxes:
        for i, v in enumerate(box):
            # print("{} {}".format(i, v))
            if i == v:
                return True
            else:
                return False
