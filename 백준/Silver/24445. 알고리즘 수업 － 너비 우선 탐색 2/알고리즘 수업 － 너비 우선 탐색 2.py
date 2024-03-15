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

visited = [0] * (n+1)

cnt = 1
def bfs(start):
    global cnt
    dq = deque([start])
    visited[start] = cnt

    while dq:
        v = dq.popleft()
        for i in graph[v]:
            if not visited[i]:
                dq.append(i)
                cnt += 1
                visited[i] = cnt

bfs(v)
for i in range(1, n+1):
    print(visited[i])