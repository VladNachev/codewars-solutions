""" Beginner Series #3 Sum of Numbers
Task Overview:
Given two integers a and b, which can be positive or negative, find the sum of all the integers between including them too and return it. If the two numbers are equal return a or b.

Note: a and b are not ordered!

Examples
get_sum(1, 0) == 1   // 1 + 0 = 1
get_sum(1, 2) == 3   // 1 + 2 = 3
get_sum(0, 1) == 1   // 0 + 1 = 1
get_sum(1, 1) == 1   // 1 Since both are same
get_sum(-1, 0) == -1 // -1 + 0 = -1
get_sum(-1, 2) == 2  // -1 + 0 + 1 + 2 = 2

Tags: FUNDAMENTALS, ALGORITHMS
https://www.codewars.com/kata/55f2b110f61eb01779000053/train/python
"""

#############################################################
#                        MY SOLUTIONS                       #
#############################################################

def get_sum(a,b):
    result_array = []
    if a > b:
        for i in range (b, a+1):
            result_array.append(i)
    else:
        for i in range (a, b+1):
            result_array.append(i)
    return sum(result_array)

#############################################################
#                           Test Cases                      #
#############################################################

Test.assert_equals(get_sum(0,1),1)
Test.assert_equals(get_sum(0,-1),-1)
