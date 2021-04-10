""" Function 2 - squaring an argument
Description: You have to write a function that takes an argument and returns the square of it.
Tags: FUNDAMENTALS
Link: https://www.codewars.com/kata/523b623152af8a30c6000027
"""

#############################################################
#                        MY SOLUTIONS                       #
#############################################################

def square(n):
    n = n * n
    return n

#############################################################
#                           Test Cases                      #
#############################################################

test.assert_equals(square(2), 4)
test.assert_equals(square(50), 2500)
test.assert_equals(square(1), 1)