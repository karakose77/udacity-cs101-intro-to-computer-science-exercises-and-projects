# Crypto Analysis: Frequency Analysis
#
# To analyze encrypted messages, to find out information about the possible
# algorithm or even language of the clear text message, one could perform
# frequency analysis. This process could be described as simply counting
# the number of times a certain symbol occurs in the given text.
# For example:
# For the text "test" the frequency of 'e' is 1, 's' is 1 and 't' is 2.
# The input to the function will be an encrypted body of text that only
# contains the lowercase letters a-z. As output you should return a list
# of the normalized frequency for each of the letters a-z. The normalized
# frequency is simply the number of occurrences, i, divided by the total
# number of characters in the message, n.


def frequency_analyzer(message):
    """
    Return the frequencies of all characters in input string,
    by counting all repetitions of a character and dividing it
    by the count of all characters.
    """
    alphabet_dict = {}
    message = "".join(message.split(" "))
    for char in list("abcdefghijklmnopqrstuvwxyz"):
        alphabet_dict[char] = 0
    for char in set(message):
        count = 0
        for check_char in message:
            count += char == check_char
        alphabet_dict[char] = count/len(message)
    return alphabet_dict


print(frequency_analyzer("aaaaa bbbbbbbbbb ccccccccccccccc" +
                         " h dddddddddddddddddddd"))
