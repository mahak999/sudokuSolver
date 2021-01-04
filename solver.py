def stringToList(input_string):
    # Function for converting inputted string of integers to list
    # of integers (Used to take puzzle's row input from user)
    num_list = input_string.split()
    list1 = []
    for element in num_list:
        list1.append(int(element))
    return list1


def checkRow(board_param, row):
    # checks for the repetition of the numbers from a specific row
    numbers_seen = set()

    for i in range(0, 9):
        if board_param[row][i] in numbers_seen:
            return False
        if board_param[row][i] != 0:
            numbers_seen.add(board_param[row][i])

    return True


def checkCol(board_param, col):
    # checks for the repetition of the numbers from a specific column
    numbers_seen = set()

    for i in range(0, 9):
        if board_param[i][col] in numbers_seen:
            return False
        if board_param[i][col] != 0:
            numbers_seen.add(board_param[i][col])

    return True


def checkBox(board_param, row_start, col_start):
    # checks for the repetition of the numbers from a small 3x3 box
    numbers_seen = set()

    for row in range(0, 3):
        for col in range(0, 3):
            curr = board_param[row + row_start][col + col_start]

            # If already encountered before,
            # return false
            if curr in numbers_seen:
                return False

            # If it is not an empty cell,
            # insert value at current cell in set
            if curr != 0:
                numbers_seen.add(curr)

    return True


def isValid(board_param, row, col):
    # checking certain row, col combination for correctness
    # row and col are divided by 3 in order to obtain the beginning of small box
    return (checkRow(board_param, row) and checkCol(board_param, col) and
            checkBox(board_param, row - row % 3, col - col % 3))


def isValidBoard(board_param, n):
    for i in range(0, n):
        for j in range(0, n):
            # if not a valid combination return false
            if not isValid(board_param, i, j):
                return False

    return True


yesNo = input(
    "In order to input a board to solve Press Y \n and if you want to use a "
    "default board Press N    ")
if yesNo == 'Y':
    print(
        "Input your 9x9 board row-wise as a list here (press 0 to signify "
        "empty cell)")
    board_row1_temp = input("Input first row as a list separated by spaces\t")
    board_row1 = stringToList(board_row1_temp)
    board_row2_temp = input("Input second row as a list separated by spaces\t")
    board_row2 = stringToList(board_row2_temp)
    board_row3_temp = input("Input third row as a list separated by spaces\t")
    board_row3 = stringToList(board_row3_temp)
    board_row4_temp = input("Input fourth row as a list separated by spaces\t")
    board_row4 = stringToList(board_row4_temp)
    board_row5_temp = input("Input fifth row as a list separated by spaces\t")
    board_row5 = stringToList(board_row5_temp)
    board_row6_temp = input("Input sixth row as a list separated by spaces\t")
    board_row6 = stringToList(board_row6_temp)
    board_row7_temp = input("Input seventh row as a list separated by spaces\t")
    board_row7 = stringToList(board_row7_temp)
    board_row8_temp = input("Input eighth row as a list separated by spaces\t")
    board_row8 = stringToList(board_row8_temp)
    board_row9_temp = input("Input ninth row as a list separated by spaces\t")
    board_row9 = stringToList(board_row9_temp)
    if (len(board_row1) != 9 or len(board_row2) != 9 or len(board_row3) != 9 or
            len(board_row4) != 9 or len(board_row5) != 9 or len(board_row6) != 9
            or len(board_row7) != 9 or len(board_row8) != 9 or len(
                board_row9) != 9):
        print("This is not a valid board (insufficient numbers to create a "
              "9x9 box).\n Restart the program to re-enter a new combination.")
        exit()

    board = [board_row1, board_row2, board_row3, board_row4, board_row5,
             board_row6, board_row7, board_row8, board_row9]

    if not isValidBoard(board, 9):
        print("This is not a valid board. Restart the program to re-enter "
              "a new combination.")
        exit()

    print("accepted")


elif yesNo == 'N':
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

else:
    print("This is not a valid selection!")
    exit()


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
        for j in range(len(board_param)):
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


def solve(board_param):
    position_found = findEmptyCell(board_param)
    if not position_found:  # if every position is filled then we got the answer
        return True
    else:
        row, col = position_found

    for i in range(1, 10):
        if valid(board_param, i, (row, col)):
            # if the inserted number is valid then insert it at that specific
            # position
            board_param[row][col] = i

            if solve(board_param):  # algorithm proceeds to check further
                # combinations
                return True
            board_param[row][col] = 0  # if the current combination is not
            # valid then set it to zero and then try another combination for
            # the previous empty cell

    return False


printBoard(board)
solve(board)
print("\n\n\n________________________________\nSolved puzzle:\n\n")
printBoard(board)
