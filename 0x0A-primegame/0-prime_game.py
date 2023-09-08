#!/usr/bin/python3
'''designing a prime game'''


def isWinner(x, nums):
    '''defining the function'''
    max = 2
    # players = 1
    result = []
    winner = ""
    if x == 0:
        return None
    if nums == []:
        return None
    for rounds in range(x):
        player = []
        mylist = []
        for num in nums:
            # players = 1
            # while players <= 2:
            listed = []
            # while true
            for no in range(1, num+1):
                listed.append(no)
                # check prime numner
                prime = []
                players = 1
                while players <= 2:
                    # for i in range(1, no+1):
                    for i in listed:
                        if i <= 1:
                            continue
                        for k in range(2, i // 2 + 1):
                            if (i % k) == 0:
                                break
                            else:
                                prime.append(i)

                            # get multiples of no
                                for j in range(1, i + 1):
                                    try:
                                        listed.remove(j*i)
                                    except ValueError:
                                        pass
                            # prime.remove(k)
                            '''for z in listed:
                            if (z % 2) == 0:
                            listed.remove(z)'''
                    # players = players + 1
                    # print (listed)

                    if all(p == 1 for p in listed):
                        player.append('maria')
                        break
                    else:
                        player.append('ben')
                        players = players + 1
                    if players == 2:
                        break
        mylist.append(listed)
        result.append(mylist)
        count1 = player.count('maria')
        count2 = player.count('ben')
        if count1 > count2:
            winner = 'Maria'
        else:
            winner = 'Ben'
        return winner
    return None
