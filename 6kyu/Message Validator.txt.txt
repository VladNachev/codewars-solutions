""" Message Validator
Task Overview:
In this kata, you have an input string and you should check whether it is a valid message. To decide that, you need to split the string by the numbers, and then compare the numbers with the number of characters in the following substring.

For example "3hey5hello2hi" should be split into 3, hey, 5, hello, 2, hi and the function should return true, because "hey" is 3 characters, "hello" is 5, and "hi" is 2; as the numbers and the character counts match, the result is true.

Notes:

Messages are composed of only letters and digits
Numbers may have multiple digits: e.g. "4code13hellocodewars" is a valid message
Every number must match the number of character in the following substring, otherwise the message is invalid: e.g. "hello5" and "2hi2" are invalid
If the message is an empty string, you should return true

Tags: ALGORITHMS
https://www.codewars.com/kata/5fc7d2d2682ff3000e1a3fbc/train/python
"""

#############################################################
#                        MY SOLUTIONS                       #
#############################################################

import re

def is_a_valid_message(message):
    arr_numbers = []
    arr_words = []
    y = 0

    # Check for empty string
    if not message:
        return True

    a = list(re.split('(\d+)',message))
    a.pop(0)

    #Spliting the message string into 2 lists
    for x in a:
        b = x.isnumeric()
        if b == True:
            arr_numbers.append(x)
        else:
            arr_words.append(x)

    for x in range(0, int(len(a)/2)):
        if int(arr_numbers[y]) != len(arr_words[y]):
            return False
            break
        else:
            if y == int(len(a)/2)-1:
                return True
        y += 1
