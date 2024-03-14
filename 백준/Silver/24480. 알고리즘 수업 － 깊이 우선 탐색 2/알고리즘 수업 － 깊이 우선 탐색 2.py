import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n, m, v = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

for i in range(1, n+1):
    graph[i].sort(reverse=True)
    
visited = [0] * (n+1)

cnt = 1

def dfs(v):
    global cnt
    visited[v] = cnt

    for i in graph[v]:
        if visited[i] == 0:
            cnt += 1
            dfs(i)

dfs(v)
for i in range(1, n+1):
    print(visited[i])