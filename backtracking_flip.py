from datetime import datetime
from itertools import combinations
import copy
import numpy as np
import math

def is_attacked_diagonal(q1, q2):
    (x1,y1) = q1
    (x2,y2) = q2

    return (x1-y1 == x2-y2) or (x1+y1 == x2+y2)

def valid_perm(perm, n):
    '''
    All valid queen position combinations must be on different rows and columns
    Consider permutations of range(n)
    Using index of the permutation as column, and value as row will return points
    that are valid under the constraint placing as if they are rooks that cannot
    each other
    Checks if last queen added is attacked/attacks any other queens
    '''

    queen1 = (len(perm)-1, perm[-1])

    for column, row  in enumerate(perm[:-1]):
        queen2 = (column, row)
        if is_attacked_diagonal(queen1,queen2):
            return False
    return True

def mirror_vertical_axis(x,n):
    return n-1-x

def print_time():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S.%f")
    print("Current Time =", current_time)

def vis_board(n, board):
    board_arr = np.zeros((n,n), dtype=int)
    for column, row in enumerate(board):
        board_arr[column, row] +=1
    
    pretty_board_string = '\n'
    queen_char = 'X'
    empty_char = '•'
    pad_char = ' '
    newline = '\n'

    for row in board_arr:
        for index, element in enumerate(row):
            if element == 0:
                pretty_board_string += empty_char
            else:
                pretty_board_string += queen_char
            if index == n - 1:
                pretty_board_string += newline
            elif index != 0 or index != n - 1:
                pretty_board_string += pad_char

    return pretty_board_string

def vis_solutions(solutions, n):
    for board in solutions:
        print('Return for next solution')
        input()
        print(vis_board(n, board))




n=13
board = []
valid_solutions = []
available_rows = list(range(n))


print_time()

def backtrack(board, n, available_rows):
    for i in range(len(available_rows)):
        iteration_rows = copy.copy(available_rows)
        iteration_board = copy.copy(board)
        iteration_board.append(iteration_rows.pop(i))
        if iteration_board[0] == math.ceil(n/2):
            return
        elif len(iteration_board) > 1:
            if valid_perm(iteration_board, len(iteration_board)):
                if len(iteration_board) == n:
                    solution = copy.copy(iteration_board)
                    valid_solutions.append(solution)
                    if not (n % 2 == 1 and solution[0] == int(n/2)):
                        valid_solutions.append(map(mirror_vertical_axis, solution, [n]*n))

                else:
                    backtrack(iteration_board, n, iteration_rows)

        else:
            backtrack(iteration_board, n, iteration_rows)

            

backtrack(board, n, available_rows)  

print(len((valid_solutions)))

print_time()
        
vis_solutions((valid_solutions), n)
