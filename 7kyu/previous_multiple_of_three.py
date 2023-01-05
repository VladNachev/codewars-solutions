def prev_mult_of_three(n):
    if n % 3 == 0:
        return n
    elif len(str(n)) == 1:
        return None
    else:
        while len(str(n)) > 1:
            n = n // 10
            if n % 3 == 0:
                return n
            elif len(str(n)) == 1:
                return None
            else:
                continue