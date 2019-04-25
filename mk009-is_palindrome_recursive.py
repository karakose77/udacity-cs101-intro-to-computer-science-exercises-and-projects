# Define a procedure, that takes as input a string, and returns a
# Boolean indicating if the input string is a palindrome.


def is_palindrome_recursive(s):
    """
    Returns true if input string is a palindrome.
    """
    if len(s) == 0 or len(s) == 1:
        return True
    return (s[0] == s[-1]) and is_palindrome_recursive(s[1:-1])
