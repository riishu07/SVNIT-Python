
import numpy as np
import random

def is_valid(queens):
    for i in range(8):
        for j in range(i+1, 8):
            if abs(queens[i] - queens[j]) == abs(i - j):
                return False
    return True

def find_solution():
    while True:
        queens = list(range(8))
        random.shuffle(queens)
        if is_valid(queens):
            return queens

def create_board(queens):
    board = np.zeros((8, 8), dtype=int)
    for row, col in enumerate(queens):
        board[row, col] = 1
    return board

solution = find_solution()
board = create_board(solution)
print(board)
