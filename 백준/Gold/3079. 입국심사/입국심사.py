N, M = map(int,input().split()) # 심사대 개수 N, 심사 받는 사람 수 M
times = [int(input()) for _ in range(N)]

start = min(times) # 심사받는 최소 시간, 동시에 들어갈 수 있기떄문에 인원수만큼 곱하지않고 그냥 찐! 최소시간으로 탐색
end = max(times) * M # 심사받는 최대 시간
answer = 0

while start<=end:
    mid = (start+end)//2 # 시간이 늘어날 수록 심사받을 수 있는 사람 수가 늘어남!
    p = sum(mid//time for time in times) # 심사받을 수 있는 사람 수
    if p < M:
        start = mid + 1 # 지금 시간에는 target보다 심사를 못받아!! -> 시간을 늘리자 start +
    else:
        end = mid - 1
        answer = mid
        
print(answer)