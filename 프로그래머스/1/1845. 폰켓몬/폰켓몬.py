## 각 배열의 요소가 중복처리를 해야함 -> 해시맵

def solution(nums):
    
    d = {}
    cnt = 0
    
    for n in nums:
        d[n] = d.get(n, 0) + 1
    
    for key in d.keys():
        cnt += 1
        
    if cnt >= len(nums)//2 :
        answer = len(nums)//2
    else:
        answer = cnt
        
    return answer