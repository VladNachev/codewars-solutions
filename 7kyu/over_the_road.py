""" Over The Road
Task Overview:
You've just moved into a perfectly straight street with exactly n identical houses on either side of the road. Naturally, you would like to find out the house number of the people on the other side of the street. The street looks something like this:

Street
1|   |6
3|   |4
5|   |2
Evens increase on the right; odds decrease on the left. House numbers start at 1 and increase without gaps. When n = 3, 1 is opposite 6, 3 opposite 4, and 5 opposite 2.

Given your house number address and length of street n, give the house number on the opposite side of the street.

Both n and address could get upto 500 billion with over 200 random tests.

Tags: FUNDAMENTALS, NUMBERS, MATHEMATICS, ALGORITHMS, PERFORMANCE
https://www.codewars.com/kata/5f0ed36164f2bc00283aed07/train/python
"""

#############################################################
#                      Usage Examples                       #
#############################################################

over_the_road(address, n)
over_the_road(1, 3) = 6
over_the_road(3, 3) = 4
over_the_road(2, 3) = 5
over_the_road(3, 5) = 8

#############################################################
#                        MY SOLUTIONS                       #
#############################################################

return n * 2 + 1 - address

#############################################################
#                           Test Cases                      #
#############################################################

import codewars_test as test
from solution import over_the_road
test.assert_equals(over_the_road(1, 3), 6)
test.assert_equals(over_the_road(3, 3), 4)
test.assert_equals(over_the_road(2, 3), 5)
test.assert_equals(over_the_road(3, 5), 8)
test.assert_equals(over_the_road(7, 11), 16)
