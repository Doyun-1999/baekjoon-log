# 딱 봐도 Greedy 냄새가남 -> 가장 인접한 두 공유기 사이의 거리를 최대로
# lst를 정렬하는 것 부터 시작하자.
N,C = map(int,input().split())
lst = [int(input()) for _ in range(N)]
lst.sort()

s = 1 # 두 점의 최소거리
e = lst[-1] - lst[0] # 두 점의 최대거리

while s<=e:
    mid = (s+e)//2
    dis, cnt = 0, 1
    
    for i in range(1,N):
        dis += lst[i] - lst[i-1]
        if dis >= mid:
            cnt += 1
            dis = 0
    if cnt >= C:
        s = mid + 1
        ans = mid
    else:
        e = mid -1
print(ans)
        
            
    