'''
If all squares are visited 
    print the solution
Else
   a) Add one of the next moves to solution vector and recursively 
   check if this move leads to a solution. (A Knight can make maximum 
   eight moves. We choose one of the 8 moves in this step).
   b) If the move chosen in the above step doesn't lead to a solution
   then remove this move from the solution vector and try other 
   alternative moves.
   c) If none of the alternatives work then return false (Returning false 
   will remove the previously added item in recursion and if false is 
   returned by the initial call of recursion then "no solution exists" )
'''

n = 6


def is_safe(x, y, board):
    if (x >= 0 and y >= 0 and x < n and y < n and board[x][y] == -1):
        return True
    return False


def print_solution(board):
    for i in range(n):
        for j in range(n):
            print(board[i][j], end=' ')
        print()


def solveKT():
    # Initialization of Board matrix  
    board = [[-1 for i in range(n)] for i in range(n)]

    # move_x and move_y define next move of Knight.  
    # move_x is for next value of x coordinate  
    # move_y is for next value of y coordinate 
    move_x = [2, 1, -1, -2, -2, -1, 1, 2]
    move_y = [1, 2, 2, 1, -1, -2, -2, -1]

    # First place of Knight 
    board[0][0] = 0

    # Step counter for knight's position 
    pos = 1

    # Checking if solution exists or not  
    if (not solveKT_util(board, 0, 0, move_x, move_y, pos)):
        print("Solution does not exist")
    else:
        print_solution(board)


def solveKT_util(board, curr_x, curr_y, move_x, move_y, pos):
    if (pos == n ** 2):
        return True

    # Try all next moves from the current coordinate x, y 
    for i in range(8):
        new_x = curr_x + move_x[i]
        new_y = curr_y + move_y[i]
        if (is_safe(new_x, new_y, board)):
            board[new_x][new_y] = pos
            if (solveKT_util(board, new_x, new_y, move_x, move_y, pos + 1)):
                return True

            # Backtracking 
            board[new_x][new_y] = -1
    return False


solveKT()

import math


def binary_search(lys, val):
    '''lys must be a sorted_array at first
    '''
    first = 0
    last = len(lys) - 1
    index = -1
    while (first <= last) and (index == -1):
        mid = (first + last) // 2
        if lys[mid] == val:
            index = mid
        else:
            if val < lys[mid]:
                last = mid - 1
            else:
                first = mid + 1
    return index


print(binary_search([10, 20, 30, 40, 50, 60], 20))


def jump_search (lys, val):
    '''lys must be a sorted_array at first'''
    length = len(lys)
    jump = int(math.sqrt(length))
    left, right = 0, 0
    while left < length and lys[left] <= val:
        right = min(length - 1, left + jump)
        if lys[right] >= val:
            break
        left += jump
    if left >= length or lys[left] > val:
        return 'no item in list'

    right = min(length - 1, right)
    i = left
    while i <= right and lys[i] <= val:
        if lys[i] == val:
            return i
        i += 1
    return 'no item in list'

print(jump_search([1,2,3,5,6,7,8],6))
