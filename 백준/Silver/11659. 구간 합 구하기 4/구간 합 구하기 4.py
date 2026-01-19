import sys
input = sys.stdin.readline

N, M = map(int,input().split()) # N은 둘째줄 리스트의 len , M은 입력받는 횟수
lst = list(map(int,input().split()))
arr = [] #누적합을 저장해놓을 테이블 
tmp = 0

# 누적합을 저장해놓는 배열
for i in range(N):
    tmp += lst[i]
    arr.append(tmp)
    
for _ in range(M):
    a, b = map(int, input().split())  # 1-indexed, a <= b 라고 가정
    if a == 1:
        answer = arr[b-1]
    else:
        answer = arr[b-1] - arr[a-2]
    print(answer)