

def gen(n, r=[]):
    """
    Returns a Pascal Triangle of n rows.
                     1
                    1 1
                   1 2 1
                  1 3 3 1
                 1 4 6 4 1
                    ...
    """
    for x in range(n):
        r = [1 if i == 0 or i == len(r)
             else r[i-1] + r[i] for i in range(len(r)+1)]
        yield r


print(list(gen(3)))
