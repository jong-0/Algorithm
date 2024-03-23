import sys
input = sys.stdin.readline

from collections import deque

n, m = map(int, input().split())
graph = [[] for i in range(n+1)]
visited = [False] * (n+1)
result = 0

for _ in range(1, m+1):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

for i in range(1, len(graph)):
    graph[i].sort()

def bfs(graph, start):
    dq = deque([start])
    visited[start] = True
    cnt = 1

    while dq:
        v = dq.popleft()
        for i in graph[v]:
            if not visited[i]:
                dq.append(i)
                visited[i] = True
        graph[v] = []

    return cnt

for i in range(1, n+1):
    if visited[i] == False:
        result += bfs(graph, i)

print(result)