from collections import deque

N, M = map(int, input().split())

graph = []

for _ in range(N):
    lst = list(map(int, input()))
    graph.append(lst)
    
#상하좌우
dx = [0,0,-1,1]
dy = [1,-1,0,0]

def bfs(x,y):
    q = deque()
    q.append((x,y))
    
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx<0 or ny<0 or nx>=N or ny>=M:
                continue
            if graph[nx][ny] == 0: #벽인 경우
                continue
            if graph[nx][ny] == 1: # 벽이아닌경우 count
                graph[nx][ny] = graph[x][y] + 1
                q.append((nx,ny))
    return graph[N-1][M-1]

print(bfs(0,0))
        