# Given a list of lists representing a n * n matrix as input,
# define a  procedure that returns True if the input is an identity matrix
# and False otherwise.


def is_identity_matrix(L):
    """
    Returns True if the input matrix is an identity matrix, False otherwise.
    """
    result = len(L) == len(L[0])
    for i in range(len(L)):
        for j in range(len(L)):
            if i == j:
                result *= (L[i][j] == 1)
            else:
                result *= (L[i][j] == 0)
    return result
    

print(is_identity_matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1]]))