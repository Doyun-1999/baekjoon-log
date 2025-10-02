from collections import deque

N, M, V = map(int, input().split())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)   # a -> b 연결
    graph[b].append(a)

def dfs(node):
        visited[node] = True
        print(node, end =' ')
        for nxt in sorted(graph[node]):
            if not visited[nxt]:
                dfs(nxt)
                
def bfs(start):
    q = deque([start])
    visited[start] = True
    while q:
        node = q.popleft()
        print(node, end =' ')
        for nxt in sorted(graph[node]):
            if not visited[nxt]:
                visited[nxt] = True
                q.append(nxt)
                

visited = [False] * (N+1)
dfs(V)
print()

visited = [False] * (N+1)
bfs(V)