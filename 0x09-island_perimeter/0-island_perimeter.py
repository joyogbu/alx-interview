#!/usr/bin/python3
'''that returns the perimeter of the island described in grid'''


def island_perimeter(grid):
    '''defining the function'''
    # base case
    if not grid:
        return 0

    M = len(grid)
    N = len(grid[0])
    count = 0

    # traverse each cell of the matrix
    for i in range(0, M):
        for j in range(0, N):
            # if the current cell is a land
            if grid[i][j] == 1:
                # check if top edge is adjacent to the water
                if i == 0 or grid[i - 1][j] == 0:
                    count = count + 1
                # check if bottom edge is adjacent to the water
                if i == M - 1 or grid[i + 1][j] == 0:
                    count = count + 1
                # check if left edge is adjacent to the water
                if j == 0 or grid[i][j - 1] == 0:
                    count = count + 1
                # check if right edge is adjacent to the water
                if j == N - 1 or grid[i][j + 1] == 0:
                    count = count + 1
    return count
