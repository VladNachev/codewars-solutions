""" Simple Fun #136: Missing Values
Task Overview:
You are given a sequence of positive ints where every element appears three times, except one that appears only once (let's call it x) and one that appears only twice (let's call it y).

Your task is to find x * x * y.

Example
For arr=[1, 1, 1, 2, 2, 3], the result should be 18

3 x 3 x 2 = 18

For arr=[6, 5, 4, 100, 6, 5, 4, 100, 6, 5, 4, 200], the result should be 4000000

200 x 200 x 100 = 4000000

Input/Output
[input] integer array arr
an array contains positive integers.

[output] an integer
The value of x * x * y

Tags: PUZZLES, GAMES
https://www.codewars.com/kata/58a66c208b88b2de660000c3/train/python
"""

#############################################################
#                        MY SOLUTIONS                       #
#############################################################

from collections import Counter

def missing_values(seq):
    thisdict = {}
    list_freq = (Counter(seq))
    
    for key, value in list_freq.items() :
        thisdict.update({ key: value })
        
    key_list = list(thisdict.keys())
    val_list = list(thisdict.values())
    position = val_list.index(2)
    y =key_list[position]
    position = val_list.index(1)
    x = key_list[position]
    
    return x * x * y
 

#############################################################
#                           Test Cases                      #
#############################################################

import codewars_test as test
from solution import missing_values

@test.describe("Example")
def test_group():
    @test.it("test case")
    def test_case():
        test.assert_equals(missing_values([1, 1, 1, 2, 2, 3]), 18)
        test.assert_equals(missing_values([96, 56, 24, 46, 75, 46, 75, 21, 46, 21, 75, 96, 56, 96, 56]), 12096)
        test.assert_equals(missing_values([27, 65, 44, 39, 44, 21, 21, 44, 65, 39, 21, 65]), 28431)
        test.assert_equals(missing_values([66, 4, 80, 66, 4, 83, 97, 81, 19, 4, 80, 51, 83, 81, 83, 66, 51, 80, 97, 81, 97]), 18411)
        test.assert_equals(missing_values([60, 76, 86, 76, 86, 53, 60, 88, 71, 71, 71, 86, 88, 76, 88, 17, 60, 26, 17, 17, 26, 53, 98, 53]), 249704)
        test.assert_equals(missing_values([42, 23, 45, 33, 33, 19, 42, 79, 79, 23, 95, 95, 79, 19, 42, 33, 19, 23]), 192375)
        test.assert_equals(missing_values([4, 74, 41, 41, 41, 88, 63, 35, 35, 4, 88, 13, 63, 74, 63, 88, 4, 74]), 5915)