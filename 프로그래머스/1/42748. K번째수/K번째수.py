def solution(array, commands):
    ans = []
    
    for i, j, k in commands:
        sub = array[i-1:j]
        sub.sort()
        ans.append(sub[k-1])
        
    return ans