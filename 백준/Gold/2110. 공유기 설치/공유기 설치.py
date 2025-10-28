N, C = map(int,input().split())
locations = [int(input()) for _ in range(N)]

locations.sort() # x좌표에 정렬하기 위해 sort
start = 1 # 두 공유기 사이의 최소거리
end = locations[-1] - locations[0] # 두 공유기 사이의 최대거리
answer = 0

while start <= end:
    mid = (start+end)//2 # 중간지점 거리
    cnt, distance = 1, 0 
    
    for i in range(1,N):
        distance += locations[i] - locations[i-1] # 두 점사이의 거리를 누적함 -> 총 길이가 누적되는 중
        if distance >= mid: # mid 값보다 더 크게
            cnt += 1 # 공유기 설치!
            distance = 0
    if cnt >= C: # mid 간격으로 공유기 설치가 되는경우!
        start = mid + 1 # Mid 값을 올려보자 -> 더 먼거리도 가능한지 반복
        answer = mid # 일단 최대값 저장
    else:
        end = mid - 1 # mid 간격으로 공유기 설치가 안되므로 -> Mid 값 낮추기!
                
print(answer)   