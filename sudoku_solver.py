import time
import random
BLANK = "#"

def read_sudoku(filename):
    with open(filename, 'r') as file:
        return [list(line.strip()) for line in file]

def is_current_board_valid(board):
    for row in board:
        if not is_valid_set_of_chunk(row):
            return False

    for col in zip(*board):
        if not is_valid_set_of_chunk(col):
            return False

    for box in get_boxes(board):
        if not is_valid_set_of_chunk(box):
            return False

    return True

##
def is_current_cross_board_valid(board):
    if not is_current_board_valid(board):
        return False

    for cross in get_cross(board):
        if not is_valid_set_of_chunk(cross):
            return False

    return True
##

def is_valid_set_of_chunk(chunk):
    chunk = [cell for cell in chunk if cell != BLANK]
    return len(chunk) == len(set(chunk))

def get_boxes(board):
    boxes = []
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            box = [board[x][y] for x in range(i, i + 3) for y in range(j, j + 3)]
            boxes.append(box)
    return boxes
##
def get_cross(board):
    cross = [[], []]
    for i, row in enumerate(board):
        cross[0].append(row[i])
        cross[1].append(row[8-i])
    return cross
##
def get_empty_cells(board):
    empty_cells = []
    for rdx, row in enumerate(board):
        for cdx, cell in enumerate(row):
            if cell == BLANK:
                empty_cells.append((rdx, cdx))
    return empty_cells

def solve_sudoku(board, valid_board_func):
    start = time.time()
    return solver(board, valid_board_func, start)

def solver(board, valid_board_func, start, timeout=1):
    if(time.time()-start > timeout):
        return False
    if not valid_board_func(board):
        return False

    empty_cells = get_empty_cells(board)
    if not empty_cells:
        return True

    rdx, cdx = empty_cells[0]
    nums = [i+1 for i in range(9)]
    random.shuffle(nums)
    for num in nums:
        board[rdx][cdx] = str(num)
        if solver(board, valid_board_func, start):
            return True
        board[rdx][cdx] = BLANK

    return False

"""def duplicated(board, num_idx): 
    duplicated = 0 
    for num, row in enumerate(num_idx): 
        for idx, (rdx, cdx) in enumerate(row): 
            for i in range(idx+1,len(row)): 
                (r,c) = num_idx[num][i] 
                s1 = board[rdx][c] 
                s2 = board[r][cdx] 
                #print("e")
                if(s1==s2): 
                    duplicated = 1 
                    print("r")
                    return duplicated 
    return duplicated

def is_duplicated(board, valid_board_func):
    num_idx = [[]for _ in range(10)] 
    for rdx, row in enumerate(board): 
        for cdx, num in enumerate(row): 
            crdx = 8-rdx
            #print("w")
            if not (valid_board_func==is_current_cross_board_valid and (rdx==cdx or crdx==cdx)):
                num_idx[int(num)].append((rdx, cdx)) 
    dupl = duplicated(board, num_idx) + 1
    return dupl"""

####
def count_solutions(board, valid_board_func, limit=2):
    empty_cells = get_empty_cells(board)
    if not empty_cells:
        return 1  # 완성된 해답 1개

    rdx, cdx = empty_cells[0]
    total = 0

    for num in range(1, 10):
        board[rdx][cdx] = str(num)

        if valid_board_func(board):
            total += count_solutions(board, valid_board_func, limit)
            if total >= limit:  # 해답 2개 이상이면 더 볼 필요 없음
                board[rdx][cdx] = BLANK
                return total

        board[rdx][cdx] = BLANK

    return total
####

def print_board(board):
    for row in board:
        print(' '.join(row))

if __name__ == "__main__":
    board = read_sudoku('sudoku.txt')
    if solve_sudoku(board, is_current_board_valid):
        print_board(board)