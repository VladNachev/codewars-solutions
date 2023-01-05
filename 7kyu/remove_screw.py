def sc(s):
    score = 0
    count = 0
    count_array = 0
    s_array = []
    for x in s:
        s_array.append(x)
    if len(s_array) == 1:
        return 1
    else:
        for i in s_array:
            score = score + 2
            count = count + 1
            if count == len(s_array):
                break
            else:
                if s_array[count_array] != s_array[count_array+1]:
                    score = score +5
            count_array = count_array + 1
        return score - 1