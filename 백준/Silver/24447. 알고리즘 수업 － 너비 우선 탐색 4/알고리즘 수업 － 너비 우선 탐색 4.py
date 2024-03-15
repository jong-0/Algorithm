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
visiteb = [0] * (n+1)

cnt = 1
def bfs(start, d):
    global cnt
    dq = deque([start])
    visited[start] = d
    visiteb[start] = cnt

    while dq:
        v = dq.popleft()
        for i in graph[v]:
            if visited[i] == -1:
                cnt += 1
                dq.append(i)
                visited[i] = visited[v] + 1
                visiteb[i] = cnt

bfs(v, 0)
sum = 0
for i in range(1, n+1):
    sum += visiteb[i] * visited[i]

print(sum)