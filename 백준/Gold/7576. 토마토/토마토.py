from collections import deque

m, n = map(int,input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int,input().split())))

def check() -> bool:
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                return False
    return True 
            
def bfs():
    q = deque()
    dx = [0,0,-1,1]
    dy = [1,-1,0,0]
        # 1️⃣ 처음부터 익은 토마토(1) 전부 큐에 넣기
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                q.append((j, i))

    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<m and 0<=ny<n and graph[ny][nx] == 0:
                q.append((nx,ny))
                graph[ny][nx] = graph[y][x] + 1
    is_full = check()
    if not is_full:
        return -1
    else:
        return max(max(row) for row in graph) - 1

def solution():
    result = bfs()
    print(result)

solution()
