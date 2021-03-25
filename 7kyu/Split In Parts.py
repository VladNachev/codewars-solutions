""" Split In Parts
Task Overview:
The aim of this kata is to split a given string into different strings of equal size (note size of strings is passed to the method)

Example:

Split the below string into other strings of size #3

'supercalifragilisticexpialidocious'

Will return a new string
'sup erc ali fra gil ist ice xpi ali doc iou s'

Assumptions:

String length is always greater than 0
String has no spaces
Size is always positive

Tags: FUNDAMENTALS, STRINGS
https:https://www.codewars.com/kata/5650ab06d11d675371000003/train/python
"""


#############################################################
#                        MY SOLUTIONS                       #
#############################################################

def split_in_parts(s, part_length):
    # b is the separator
    # the join() method will join all the items into a string
    b= " "
    return b.join([s[i:i + part_length] for i in range(0, len(s), part_length)])

#############################################################
#                           Test Cases                      #
#############################################################

@test.describe('Example Tests')
def example_tests():
    test.assert_equals(split_in_parts("supercalifragilisticexpialidocious", 3), "sup erc ali fra gil ist ice xpi ali doc iou s")
    test.assert_equals(split_in_parts("HelloKata", 1), "H e l l o K a t a")
    test.assert_equals(split_in_parts("HelloKata", 9), "HelloKata")