def invert(lst):
    lst_2 = []
    for x in lst:
        if x < 0:
            x = x * (-1)
            lst_2.append(x)
        elif x > 0:
            x = x * (-1)
            lst_2.append(x)
        else:
            lst_2.append(x)
    return lst_2