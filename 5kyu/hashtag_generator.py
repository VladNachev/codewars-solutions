""" The Hashtag Generator
Task Overview:
The marketing team is spending way too much time typing in hashtags.
Let's help them with our own Hashtag Generator!

Here's the deal:

It must start with a hashtag (#).
All words must have their first letter capitalized.
If the final result is longer than 140 chars it must return false.
If the input or the result is an empty string it must return false.

Examples:

" Hello there thanks for trying my Kata"  =>  "#HelloThereThanksForTryingMyKata"
"    Hello     World   "                  =>  "#HelloWorld"
""                                        =>  false

Tags: STRINGS, ALGORITHMS
https://www.codewars.com/kata/52449b062fb80683ec000024
"""
#############################################################
#                        MY SOLUTIONS                       #
#############################################################

def generate_hashtag(s):
    arr = ["#"]
    y = "check"
    i = 1
    if s == "":
        return False
    for x in s:
        if ' ' in x:
            y = x
            continue
        else:
            if y == " ":
                arr.append(x.upper())
            elif i == 1:
                arr.append(x.upper())
            else:
                arr.append(x.lower())
            y = "check"
        i = i + 1
    if len(arr) > 140:
        return False
    else: 
        return "".join(arr)