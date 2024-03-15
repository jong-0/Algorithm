from collections import deque
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, m, v = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

for i in range(1, n+1):
    graph[i].sort(reverse=True)

visited = [-1] * (n+1)

def bfs(start, d):
    dq = deque([start])
    visited[start] = d

    while dq:
        v = dq.popleft()
        for i in graph[v]:
            if visited[i] == -1:
                dq.append(i)
                visited[i] = visited[v] + 1

bfs(v, 0)
for i in range(1, n+1):
    print(visited[i])