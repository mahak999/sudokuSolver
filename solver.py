yesNo = input(
    "In order to input a board to solve Press Y \n and if you want to use a "
    "default board Press N    ")
if yesNo == 'Y':
    print(
        "Input your board row-wise as a list here (press 0 to signify empty "
        "cell)")
    board_row1 = input("Input first row")
    board_row2 = input("Input second row")
    board_row3 = input("Input third row")
    board_row4 = input("Input fourth row")
    board_row5 = input("Input fifth row")
    board_row6 = input("Input sixth row")
    board_row7 = input("Input seventh row")
    board_row8 = input("Input eighth row")
    board_row9 = input("Input ninth row")
    board = [board_row1, board_row2, board_row3, board_row4, board_row5, \
             board_row6, board_row7, board_row8, board_row9]
else:
    board = [[7, 8, 0, 4, 0, 0, 1, 2, 0],
             [6, 0, 0, 0, 7, 5, 0, 0, 9],
             [0, 0, 0, 6, 0, 1, 0, 7, 8],
             [0, 0, 7, 0, 4, 0, 2, 6, 0],
             [0, 0, 1, 0, 5, 0, 9, 3, 0],
             [9, 0, 4, 0, 6, 0, 0, 0, 5],
             [0, 7, 0, 3, 0, 0, 0, 1, 2],
             [1, 2, 0, 0, 0, 7, 4, 0, 0],
             [0, 4, 9, 2, 0, 6, 0, 0, 7],
             ]


def printBoard(board_param):
    for i in range(len(board_param)):
        if i % 3 == 0 and i != 0:
            print("-------------------------")
        for j in range(len(board_param[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")
            if j == 8:
                print(str(board_param[i][j]))
            else:
                print(str(board_param[i][j]) + " ", end="")


def findEmptyCell(board_param):
    """
    Finds and returns the postion of an empty cell in the board
    :param board_param: a nested list representing the board
    :return: a tuple representing the position of the empty cell in #row, #column format
    """
    for i in range(len(board_param)):
        for k in range(len(board_param)):
            if board_param[i][j] == 0:
                return i, j
    return None


def valid(board_param, num, pos):
    # checking the row for a valid combination
    for i in range(len(board_param[0])):
        if board_param[pos[0]][i] == num and pos[1] != i:
            # checking if the number we have added is already in the row and
            # then not caring about the case when we have just added that
            # number at the position
            return False

    # checking the column for a valid combination
    for i in range(len(board_param[0])):
        if board_param[i][pos[1]] == num and pos[0] != i:
            # checking if the number we have added is already in the coulumn
            # and then not caring about the case when we have just added that
            # number at the position
            return False

    # checking the small box for a valid combination
    box_x = pos[0] // 3  # row_number//3 (small-box's row position)
    box_y = pos[1] // 3  # column_number//3 (small-box's column position)

    for i in range(box_x * 3, box_x * 3 + 3):
        for j in range(box_y * 3, box_y * 3 + 3):
            if board_param[i][j] == num and (i, j) != pos:
                return False

    return True



