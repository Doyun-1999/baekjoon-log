from collections import deque

def bfs(x,y, maps):
    n = len(maps) # 행(가로) ->y축 -> (0,n) -> 리스트에선 maps[n][0]
    m = len(maps[0]) # 열(세로) -> (m,0) -> 리스트에선 maps[0][m]
    
    q = deque()
    q.append((x,y))
    
    dx = [0,0,-1,1]
    dy = [1,-1,0,0]
    
    #maps[y][x] = 0 # 방문 처리
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<m and 0<=ny<n and maps[ny][nx] == 1:
                maps[ny][nx] = maps[y][x] + 1
                q.append((nx,ny))
    
    if maps[n-1][m-1] == 1:
        return -1
    else:
        return maps[n-1][m-1]
            
def solution(maps):
    return bfs(0,0, maps)