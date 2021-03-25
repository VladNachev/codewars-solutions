""" Break camelCase
Task Overview:

Complete the solution so that the function will break up camel casing, using a space between words.

Example:

solution("camelCasing")  ==  "camel Casing"

Tags: FUNDAMENTALS, STRINGS, FORMATTING, ALGORITHMS
https://www.codewars.com/kata/5208f99aee097e6552000148/train/python
"""

#############################################################
#                        MY SOLUTIONS                       #
#############################################################

import re

def solution(s):
    arr_s = []
    for x in s:
        a = x
        a = a.isupper()
        if a == True:
            break
        arr_s.append(x)
    return ''.join(arr_s) + " " + ' '.join(re.findall('[A-Z][^A-Z]*', s))
