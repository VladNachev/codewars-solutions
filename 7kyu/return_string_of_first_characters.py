def make_string(s):
    make_string_list = list(s.split(" "))
    result_list = []
    y = 0
    for i in range(0, len(make_string_list)):
        result_list.append(make_string_list[y][:1])
        y= y + 1
    return ''.join(result_list)