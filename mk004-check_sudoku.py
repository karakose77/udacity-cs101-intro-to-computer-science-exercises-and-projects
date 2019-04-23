# Use the numbers 1 to 9 each nine times to complete the grid
# in such a way that the horizontal,  vertical,  and two main diagonal lines
# all add up to the same total."

# input: 9x9 matrix
# output: boolean

check_list = [n + 1 for n in range(9)]


def check_sudoku(m):
    """
    Returns true if given sudoku matrix is valid.
    """
    return check_rows(m) and check_columns(m) and check_squares(m)


def check_rows(m):
    """
    Returns true if the rows of given sudoku matrix is valid.
    """
    for row in m:
        for item in check_list:
            if item not in row:
                return False
    return True


def check_columns(m):
    """
    Returns true if the columns of given sudoku matrix is valid.
    """
    return check_rows(transpose(m))


def transpose(m):
    """
    Returns the transpose of given matrix.
    """
    tr_v = []
    for i in range(9):
        tr_v.append(0)
    tr_m = []
    for i in range(9):
        tr_m.append(tr_v[:])
    for i in range(9):
        for j in range(9):
            tr_m[j][i] = m[i][j]
    return tr_m


def check_squares(m):
    """
    Returns true if the squares of given sudoku matrix is valid.
    """
    factor = 3
    for k in range(3):
        for l in range(3):
            square = []
            for i in range(3):
                for j in range(3):
                    square.append(m[i+factor*k][j+factor*l])
            for item in check_list:
                if item not in square:
                    return False
    return True


VALID = [[4, 3, 5, 2, 6, 9, 7, 8, 1],
         [6, 8, 2, 5, 7, 1, 4, 9, 3],
         [1, 9, 7, 8, 3, 4, 5, 6, 2],
         [8, 2, 6, 1, 9, 5, 3, 4, 7],
         [3, 7, 4, 6, 8, 2, 9, 1, 5],
         [9, 5, 1, 7, 4, 3, 6, 2, 8],
         [5, 1, 9, 3, 2, 6, 8, 7, 4],
         [2, 4, 8, 9, 5, 7, 1, 3, 6],
         [7, 6, 3, 4, 1, 8, 2, 5, 9]]

print(check_sudoku(VALID))
