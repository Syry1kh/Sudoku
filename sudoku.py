def print_board(board):
    for row in board:
        line = map(str, row)
        print(" ".join(line))



def inspect_board(board, row, col, num):
    start_row = row // 3 * 3
    start_col = col // 3 * 3

    if num in board[row]:
        return False

    for i in range(9):
        if board[i][col] == num:
            return False

    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False
    return True


def search_for_an_empty_cell(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return i,j
    return None


def solve(board):
    if search_for_an_empty_cell(board) == None:
        return True
    row, col = search_for_an_empty_cell(board)
    for num in range(1, 10):
        if inspect_board(board, row, col, num):
            board[row][col] = num
            if solve(board) == True:
                return True
            board[row][col] = 0

    return False












main_lst = [
    [6, 2, 0, 0, 1, 7, 0, 0, 0],
    [7, 0, 0, 0, 8, 0, 6, 4, 0],
    [0, 0, 0, 5, 0, 0, 0, 0, 0],

    [2, 7, 0, 1, 0, 0, 8, 0, 0],
    [0, 0, 0, 9, 0, 0, 0, 0, 0],
    [0, 5, 0, 0, 7, 4, 0, 0, 0],

    [0, 0, 0, 8, 5, 6, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 2, 0, 0],
    [0, 0, 0, 2, 0, 3, 0, 9, 5]
]

if solve(main_lst):
    print_board(main_lst)
else:
    print("No solution")