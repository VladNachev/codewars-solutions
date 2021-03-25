""" Two to One
Task Overview:
Take 2 strings s1 and s2 including only letters from ato z. Return a new sorted string, the longest possible, containing distinct letters - each taken only once - coming from s1 or s2.

Examples:
a = "xyaabbbccccdefww"
b = "xxxxyyyyabklmopq"
longest(a, b) -> "abcdefklmopqwxy"

a = "abcdefghijklmnopqrstuvwxyz"
longest(a, a) -> "abcdefghijklmnopqrstuvwxyz"

Tags: FUNDAMENTALS
https://www.codewars.com/kata/5656b6906de340bd1b0000ac/train/python
"""

#############################################################
#                        MY SOLUTIONS                       #
#############################################################

    b1 = ''.join(dict.fromkeys(a1))
    b2 = ''.join(dict.fromkeys(a2))
    return ''.join(sorted(''.join(dict.fromkeys(b1 + b2))))

#############################################################
#                           Test Cases                      #
#############################################################

import codewars_test as test
    
@test.describe("longest")
def tests():
    @test.it("basic tests")
    def basics():
        test.assert_equals(longest("aretheyhere", "yestheyarehere"), "aehrsty")
        test.assert_equals(longest("loopingisfunbutdangerous", "lessdangerousthancoding"), "abcdefghilnoprstu")
        test.assert_equals(longest("inmanylanguages", "theresapairoffunctions"), "acefghilmnop
