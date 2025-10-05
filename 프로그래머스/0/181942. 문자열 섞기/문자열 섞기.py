def solution(str1, str2):
    l = len(str1)
    lst = []
    for i in range(l):
        lst.append(str1[i])
        lst.append(str2[i])
    answer = ''.join(lst)
    return answer