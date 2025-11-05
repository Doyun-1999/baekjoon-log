def solution(n, times):
    
    start =  1 # 최솟값
    end = max(times)*n # 최대값
    answer = 0
    
    while start<=end:
        mid = (start+end)//2
        p = sum(mid//time for time in times)
        if p < n:
            start = mid + 1
        else:
            end = mid - 1
            answer = mid
            
    return answer