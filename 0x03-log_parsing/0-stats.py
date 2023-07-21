#!/usr/bin/python3
'''script that reads stdin line by line and computes metrics'''


import sys


count = 0
my_list = []
# item_list = []
for line in sys.stdin:
    item_list = []
    byte_list = []
    byte_list2 = []
    dictionary = {}
    total = 0
    my_list.append(line)
    count = count + 1
    # my_dict.append(line)
    if (count == 10):
        # my_list.append(line)
        # print(my_list)
        for item in my_list:
            # dictionary = {}
            item2 = item.split()
            # if item2[-2] not in item_list:
            item_list.append(item2[-2])
            byte_list.append(item2[-1])
            byte_list2 = map(int, byte_list)
            total = sum(byte_list2)
            dictionary[item2[-2]] = dictionary.get(item2[-2], 0) + 1
        # count = 0
        # print(item_list)
        # print(dictionary)
        print("File size: {}".format(total))
        for k, v in dictionary.items():
            print("{}: {}".format(k, v))
        count = 0
