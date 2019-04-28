# Question 8: Longest Repetition

# Define a procedure, longest_repetition, that takes as input a
# list, and returns the element in the list that has the most
# consecutive repetitions. If there are multiple elements that
# have the same number of longest repetitions, the result should
# be the one that appears first. If the input list is empty,
# it should return None.


def longest_repetition(lst):
    """
    Takes as input a list, and returns the element in the list that has the
    most consecutive repetitions. If there are multiple elements that have
    the same number of longest repetitions, returns the one that appears
    first. If the input list is empty, returns None.
    """
    most_element = None
    most_count = 0
    current_element = None
    current_count = 0
    for item in lst:
        if current_element != item:
            current_element = item
            current_count = 1
        else:
            current_count += 1
        if current_count > most_count:
            most_element = current_element
            most_count = current_count
    return most_element


print(longest_repetition([1, 2, 2, 3, 3, 3, 2, 2, 1]))
# 3

print(longest_repetition(['a', 'b', 'b', 'b', 'c', 'd', 'd', 'd']))
# b

print(longest_repetition([1, 2, 3, 4, 5]))
# 1

print(longest_repetition([]))
# None
