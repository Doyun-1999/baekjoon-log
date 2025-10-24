N, M = map(int,input().split()) # N: 입국심사대의 개수 , M: 사람 수
times = [int(input()) for _ in range(N)]
 
# 이진 탐색을 위한 left와 right 설정
left, right = min(times), max(times) * M
 
while left <= right:
    mid = (left + right) // 2
    
    # mid 시간동안 심사할 수 있는 총 사람 수 계산
    total_people = sum(mid // time for time in times)
    
    # 모든 사람을 심사할 수 있는 경우
    if total_people >= M:
        answer = mid
        right = mid - 1
    # 모든 사람을 심사할 수 없는 경우
    else:
        left = mid + 1
print(answer)