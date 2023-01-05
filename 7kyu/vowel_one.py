def vowel_one(s):
    vowel_arr = ['a', 'e', 'i', 'o', 'u']
    one_and_zero = []
    for x in s:
        if x.lower() in vowel_arr:
            one_and_zero.append("1")
        else:
            one_and_zero.append("0")
    return ''.join(one_and_zero)