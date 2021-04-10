"""Move 10
Task Overview:

Move every letter in the provided string forward 10 letters through the alphabet.

If it goes past 'z', start again at 'a'.

Input will be a string with length > 0.

Tags: FUNDAMENTALS, STRINGS, ARRAYS
https://www.codewars.com/kata/57cf50a7eca2603de0000090/train/python
"""

#############################################################
#                        MY SOLUTIONS                       #
#############################################################

def move_ten(st):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    st_array = []
    result_array = []
    st_array = map(str, st)
    for x in st_array:
        if x in alphabet:
            a = alphabet.index(x)
            if a > 12:
                result_array.append(alphabet[10 - (26 - a)])

            else:
                result_array.append(alphabet[a + 10])
    return ''.join(result_array)