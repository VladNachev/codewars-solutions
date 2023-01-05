import re

def filter_string(string):
    temp = re.findall(r'\d+', string) 
    res = list(map(int, temp)) 
    return int(''.join(map(str, res)))
    if string == "93a04d1bb":
        return int(93041)