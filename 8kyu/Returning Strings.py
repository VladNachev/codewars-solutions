""" Returning Strings
Task Overview:
Make a function that will return a greeting statement that uses an input; your program should return, "Hello, <name> how are you doing today?".

Tags: FUNDAMENTALS, STRINGS
Link: https://www.codewars.com/kata/55a70521798b14d4750000a4
"""

#############################################################
#                      Usage Examples                       #
#############################################################

"Hello, <name> how are you doing today?".

#############################################################
#                        MY SOLUTIONS                       #
#############################################################

def greet(name):
    return "Hello, " + name + " how are you doing today?"

#############################################################
#                           Test Cases                      #
#############################################################

@test.describe("Fixed Tests")
def basic_tests():
    test.assert_equals(greet('Ryan'), "Hello, Ryan how are you doing today?")
    test.assert_equals(greet('Shingles'), "Hello, Shingles how are you doing today?")
