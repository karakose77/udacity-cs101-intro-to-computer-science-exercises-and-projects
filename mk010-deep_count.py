def is_list(p):
    """
    Returns if given variable is a list or not.
    """
    return isinstance(p, list)


def deep_count(p, result=0):
    """
    Count the number of deepest single elements in a list.
    If an element is also a list add the count of that list
    to the previous count.
    """
    element_count = 0
    for element in p:
        element_count += 1
        if is_list(element):
            element_count += deep_count(element)
    return element_count


print(deep_count([1, 2, [3, 4, [5, 6, 7, 8, [], [1]]]]))
