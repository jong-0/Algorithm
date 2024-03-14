from collections import deque

n, m, v = map(int, input().split())

graph = [[] for i in range(n+1)]

for i in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

for i in range(1, len(graph)):
    graph[i].sort()

visited = [False] * len(graph)
visiteb = [False] * len(graph)

def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')

    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

def bfs(graph, start, visiteb):
    dq = deque([start])
    visiteb[start]= True

    while dq:
        v = dq.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visiteb[i]:
                dq.append(i)
                visiteb[i] = True

dfs(graph, v, visited)
print()
bfs(graph, v, visiteb)