# An nxn square is called antisymmetric if A[i][j]=-A[j][i]
# for each i=0,1,...,n-1 and for each j=0,1,...,n-1.


def is_anti_symmetric(L):
    """
    Returns True if the input matrix is anti-symmetric, False otherwise.
    """
    result = len(L) == len(L[0])
    for i in range(len(L)):
        for j in range(len(L)):
            result *= L[i][j] == -L[j][i]
    return result


print(is_anti_symmetric([[0, -1, -1], [1, 0, -1], [1, 1, 0]]))
print(is_anti_symmetric([[0, -1, -1], [1, 1, -1], [1, 1, 0]]))
