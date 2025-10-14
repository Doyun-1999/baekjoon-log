## dfs와 bfs 모두 풀어보자
from collections import deque

def bfs(numbers, target):
    q = deque()    
    q.append((0,0)) # (index, total_sum)
    answer = 0
    
    while q:
        i, total_sum = q.popleft()  
        if i == len(numbers):
            if total_sum == target:
                answer += 1
            continue
            
        q.append((i + 1, total_sum + numbers[i]))
        q.append((i + 1, total_sum - numbers[i]))
    return answer   
def solution(numbers, target):
    return bfs(numbers, target)