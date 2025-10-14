from collections import deque

#n,m 입력 받기
n, m = map(int,input().split())

max_num = 100000
visited = [0] * (max_num + 1)

def dfs():
    q = deque()
    q.append(n)
    while q:
        x = q.popleft()
        if x == m:
            print(visited[x])
            break
        for nxt in (x-1, x+1, 2*x):
            if 0 <=nxt <= max_num and visited[nxt] == 0:
                visited[nxt] = visited[x] + 1
                q.append(nxt)
dfs()