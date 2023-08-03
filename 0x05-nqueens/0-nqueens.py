#!/usr/bin/python3
'''solving nqueens puzzle'''


import sys


if len(sys.argv) < 2:
    print('Usage: nqueens N')
    exit(1)
try:
    arg1 = int(sys.argv[1])
except ValueError:
    print('N must be a number')
    exit(1)
if int(sys.argv[1]) < 4:
    print('N must be at least 4')
    exit(1)
else:
    my_list = []
    #my_l = []
    for i in range(0, arg1):
        my_l = []
        for j in range(0, arg1-2):
            my_l.append(j)
        my_list.append(my_l)
    print (my_list)
