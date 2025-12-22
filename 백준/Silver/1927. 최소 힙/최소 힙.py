import sys
import heapq

# input() 대신 이거 쓰면 엄청 빨라짐
input = sys.stdin.readline

N = int(input())
arr = []
for _ in range(N):
    num = int(input())
    if num == 0: # 가장 작은값 출력 + 배열에서 제거
        if arr:
            min = heapq.heappop(arr) 
            print(min)
        else:
            print(0)
    else:
        heapq.heappush(arr, num)