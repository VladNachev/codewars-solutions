"""Rearange Number to Get its Maximum
Task Overview:

Create function that takes one positive three digit integer and rearranges its digits to get maximum possible number. Assume that argument is integer. Return null (nil for ruby) if argument is not valid.

#Examples:

maxRedigit(123); // returns 321

Tags: FUNDAMENTALS, ARITHMETIC, MATHEMATICS, ALGORITHMS, NUMBERS, CONTROL FLOW, BASIC LANGUAGE FEATURES, INTEGERS
https://www.codewars.com/kata/563700da1ac8be8f1e0000dc/train/python
"""

#############################################################
#                        MY SOLUTIONS                       #
#############################################################

def max_redigit(num):
    if num <= 0:
        return None

    num_array = list(map(int, str(num)))
    sorted(num_array)

    if len(num_array) != 3:
        return None

    return int(''.join(map(str, reversed(sorted(num_array)))))