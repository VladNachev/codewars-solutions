""" Difference of Volumes of Cuboids
Task Overview:
In this simple exercise, you will create a program that will take two lists of integers, a and b. Each list will consist of 3 positive integers above 0, representing the dimensions of cuboids a and b. You must find the difference of the cuboids' volumes regardless of which is bigger.

For example, if the parameters passed are ([2, 2, 3], [5, 4, 1]), the volume of a is 12 and the volume of b is 20. Therefore, the function should return 8.

Your function will be tested with pre-made examples as well as random ones.

Tags: FUNDAMENTALS,
https://www.codewars.com/kata/58cb43f4256836ed95000f97/train/python
"""

#############################################################
#                        MY SOLUTIONS                       #
#############################################################

from functools import reduce

def find_difference(a, b):
     result_a = reduce((lambda x, y: x * y), a)
     result_b = reduce((lambda x, y: x * y), b)
     if result_a >= result_b:
         return result_a - result_b
     else:
         result_b - result_a