N = int(input())
meetings = [tuple(map(int, input().split())) for _ in range(N)]
# 두 번째 원소 기준으로 오름차순 정렬
# 끝나는 시간이 짧은 순으로 정렬
meetings.sort(key=lambda x: (x[1],x[0]))

cnt = 1 # 
last_meeting = meetings[0][1] # 초기 미팅시간 설정

for i in range(1, N):
    # 마지막 회의시간을 기록하고 그거보다 큰경우에 갱신
    if meetings[i][0]>=last_meeting:
        cnt += 1
        last_meeting = meetings[i][1]
print(cnt)