""" Sum The Strings
Task Overview:
Create a function that takes 2 positive integers in form of a string as an input, and outputs the sum (also as a string):

  sum_str("4", "5")    # should output "9"
  sum_str("34", "5")   # should output "39"
If either input is an empty string, consider it as zero.

Tags: FUNDAMENTALS,
https://www.codewars.com/kata/5966e33c4e686b508700002d/train/python
"""

#############################################################
#                        MY SOLUTIONS                       #
#############################################################

def sum_str(a, b):
    if a and not b:
        return str(a)
    elif b and not a:
        return str(b)
    elif not a and not b:
        return "0"
    else:
        c = int(a) + int(b)
        return str(c)


#############################################################
#                           Test Cases                      #
#############################################################

import codewars_test as test
from solution import sum_str

@test.describe("Fixed Tests")
def basic_tests():
    
    @test.it("Sample Tests")
    def sample_tests():
        test.assert_equals(sum_str("4","5"), "9")
        test.assert_equals(sum_str("34","5"), "39")

    @test.it("Tests with empty strings")
    def empty_string():
        test.assert_equals(sum_str("9",""), "9", "x + empty = x")
        test.assert_equals(sum_str("","9"), "9", "empty + x = x")
        test.assert_equals(sum_str("","") , "0", "empty + empty = 0")