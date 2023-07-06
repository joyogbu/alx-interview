#!/usr/bin/python3
'''lockboxes implementation'''


def canUnlockAll(boxes) :
    '''defining the function'''
    for box in boxes:
        for i, v in enumerate(box):
            print("{} {}".format(i, v))
            if i == v:
                return True
            else:
                return False

'''boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
#boxes = [[1], [2], [3], [4], []]
canUnlockAll(boxes)'''
