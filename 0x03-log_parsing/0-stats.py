#!/usr/bin/python3
'''script that reads stdin line by line and computes metrics'''


import sys


count = 0
my_dict = {}
for line in sys.stdin:
    count = count + 1
    if (count == 10):
        print(line)
