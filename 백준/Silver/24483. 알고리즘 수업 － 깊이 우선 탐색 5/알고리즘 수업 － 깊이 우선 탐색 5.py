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
    graph[i].sort()

visited = [-1] * (n+1)
visiteb = [0] * (n+1)
cnt = 1
def dfs(v, d):
    global cnt
    visited[v] = d
    visiteb[v] = cnt

    for i in graph[v]:
        if visited[i] == -1:
            cnt += 1
            dfs(i, d+1)

dfs(v,0)
sum = 0
for i in range(1, n+1):
    sum += visiteb[i] * visited[i]
print(sum)