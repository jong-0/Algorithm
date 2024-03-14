import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n, m, v = map(int, input().split())
graph = [[] for _ in range(1+n)]

for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

for i in range(1, n+1):
    graph[i].sort(reverse=True)

visited = [-1] * (n+1)

def dfs(v, d):
    visited[v] = d

    for i in graph[v]:
        if visited[i] == -1:
            dfs(i, d+1)

dfs(v,0)
for i in range(1, n+1):
    print(visited[i])