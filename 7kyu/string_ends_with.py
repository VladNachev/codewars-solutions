def solution(string, ending):
    string_array = []
    ending_array = []
    sample_array = []
    count = 0
    for x in string:
        string_array.append(x)
    for i in ending:
        ending_array.append(i)
    ending_len = len(ending_array)
    if ending_len == 0:
        return True
    else:
        for a in reversed(string_array):
            if count >= ending_len:
                break
            sample_array.append(a)
            count += 1
        sample_array.reverse()
        if ending_array == sample_array:
            return True
        else:
            return False