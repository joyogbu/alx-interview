#!/usr/bin/python3
''' pascal triangle '''


def factorial(n):
    '''define factorial of a number'''
    if (n == 0):
        return 1
    elif (n == 1):
        return 1
    else:
        return (n * factorial(n - 1))


# mylist = []
def pascal_triangle(n):
    '''defining the function'''
    e_list = [[]]
    # mylist = []
    listing = []
    if n <= 0:
        print(e_list)
    else:
        for i in range(n):
            mylist = []
            for j in range(i+1):
                # mylist = []
                elem = factorial(i) // (factorial(j) * factorial(i - j))
                mylist.append(elem)
            listing.append(mylist)
            # print(listing)
            # print(elem, end=" ")
            # print(listing)
            # print(mylist)
    # print('\n')
    return(listing)

# print(pascal_triangle(5))
