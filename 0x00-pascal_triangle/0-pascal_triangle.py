#!/usr/bin/env python3
''' pascal triangle '''


def pascal_triangle(n):
    e_list = []
    # mylist = []
    if n <= 0:
        return (e_list)
    for i in range(n):
        for j in range(i+1):
            mylist = []
            elem = (factorial(i) // (factorial(j) * factorial(i - j)))
            mylist.append(elem)
        return(mylist)
    print('\n')


print(pascal_triangle(5))
