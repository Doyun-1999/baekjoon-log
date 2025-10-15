# 상당히 아이스크림인가? 그문제랑 비슷하다.
# 입력을 받는게 좀 독특한데, 좌표형태로 (x,y)로 받아서 그래프를 그리면될거같다!
# 입력을 받고, 그래프 탐색하면서 상하좌우 dfs 해보자 
# 내가 못하는 부분은 좌표형태로 이중리스트 받는부분..?
import sys
sys.setrecursionlimit(10000)

T = int(input())

dx = [0,0,-1,1]
dy = [1,-1,0,0]

def dfs(x,y):
    if visited[y][x] == 0:
        return
    visited[y][x] = 0 # 방문 처리
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if 0<=nx<m and 0<=ny<n and visited[ny][nx] == 1:
            dfs(nx,ny)
            
for _ in range(T):
    m,n,k = map(int,input().split())# m 가로, n 세로, k 배추 개수
    visited = [[0]*m for _ in range(n)]
    
    for _ in range(k): #배추넣기!
        x, y = map(int,input().split())
        visited[y][x] = 1
    cnt = 0
    for i in range(n):
        for j in range(m):
            if visited[i][j] == 1:
                dfs(j,i)
                cnt += 1
    print(cnt)
