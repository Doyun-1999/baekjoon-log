import sys
input = sys.stdin.readline

n, m = map(int, input().split())
lst = list(map(int, input().split()))

start = 0
end = max(lst)
total = 0
answer = 0

# mid 는 실제 나무를 자르는 값과 반비례
# 덜 자름 -> 더 많이 자르기 위해서 mid를 늘임
    
while start<=end:
    total = 0
    mid = (start+end)//2
    for tree in lst:
        if tree>mid:
            total += tree - mid
            if total >= m:
                break
    if total >= m: # 실제 자른양 >= 목표치 (과하게 자름)
        answer = mid
        start = mid + 1 # 이전보다 조금만 짤라야겠다 ~ mid 값을 올려야지(start를 높이자)
    else: # 실제 자른 양 < 목표 치 (덜 자름)
        end = mid -1 #이전보다 많이 짤라야겠다~ mid 값을 낮춰야지(end값을 낮추자)
        
print(answer)