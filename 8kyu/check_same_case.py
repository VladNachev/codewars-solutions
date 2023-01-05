def same_case(a, b): 
    an_uppercase_check_1 = a.isupper()
    an_uppercase_check_2 = b.isupper()
    letter_check_1 = a.isalpha()
    letter_check_2 = b.isalpha()
    if letter_check_1 is False or letter_check_2 is False:
        return -1
    elif an_uppercase_check_1 is True and an_uppercase_check_2 is True:
        return 1
    elif an_uppercase_check_1 is False and an_uppercase_check_2 is False:
        return 1
    else:
        return 0