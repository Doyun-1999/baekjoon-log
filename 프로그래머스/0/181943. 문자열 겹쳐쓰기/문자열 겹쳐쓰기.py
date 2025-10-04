def solution(my_string, overwrite_string, s):
    l = len(overwrite_string)
    lst = list(my_string)
    for i in range(l):
        lst[s+i] = overwrite_string[i]
    answer = ''.join(lst)
    return answer