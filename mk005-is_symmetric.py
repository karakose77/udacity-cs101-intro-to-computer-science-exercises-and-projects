# A list is symmetric if the first row is the same as the first column,
# the second row is the same as the second column and so on. Write a
# procedure, symmetric, which takes a list as input, and returns the
# boolean True if the list is symmetric and False if it is not.


def is_symmetric(L):
    """
    Returns True if given list is symmetric.
    """
    result = len(L) == len(L[0])
    for i in range(len(L)):
        for j in range(len(L)):
            result *= L[i][j] == L[j][i]
    return result
