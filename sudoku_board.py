import sudoku_solver
import random
import copy

def make_empty():
    board = [["#" for _ in range(9)] for _ in range(9)]
    return board

def random_box():
    box = [str(i+1) for i in range(9)]
    random.shuffle(box)
    return box

def random_board(board, a):#a : 1~9
    box = random_box()
    row = (a-1)//3 * 3
    col = (a-1)%3 * 3
    for r in range(row, row+3):
        for c in range(col, col+3):
            board[r][c] = box[(r-row)*3 + (c-col)]

def random_del(board, mode_func, level):
    if (level=='easy'): lev = 37
    elif (level=='normal'): lev = 42
    elif (level=='hard'): lev = 47
    delarr = [i for i in range(81)]
    while True:
        board_tmp = copy.deepcopy(board)
        random.shuffle(delarr)
        for c, i in enumerate(delarr):
            if (c>lev):
                break
            row = i//9
            col = i%9
            board_tmp[row][col] = "#"
        test = copy.deepcopy(board_tmp)
        if sudoku_solver.solve_sudoku(test, mode_func):
            return board_tmp

def valid_random_board(board, a, mode_func):
    random_board(board, a)
    while not mode_func(board):
        random_board(board, a)
    #sudoku_solver.solve_sudoku(board, mode_func)
    return board


def make_random(mode, level):
    if mode=='original':
        mode_func = sudoku_solver.is_current_board_valid
    elif mode=='cross':
        mode_func = sudoku_solver.is_current_cross_board_valid
    duplicated = 0
    while (duplicated!=1):
        board_init = make_empty()
        board = valid_random_board(board_init, 5, mode_func)
        while(not sudoku_solver.solve_sudoku(board, mode_func)):
            board = copy.deepcopy(board_init)
            for i in [2, 9]:
                valid_random_board(board, i, mode_func)
        board_deled = random_del(board, mode_func, level)
        board = copy.deepcopy(board_deled)
        duplicated = sudoku_solver.count_solutions(board, mode_func)
        


    return board_deled
#sudoku_solver.solve_sudoku(board, sudoku_solver.is_current_board_valid)