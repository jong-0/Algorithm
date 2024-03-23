from collections import deque

n = int(input())
graph = []
result = []

for _ in range(n):
    graph.append(list(map(int, input())))

def bfs(graph, x, y):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    dq = deque()
    dq.append((x, y))
    graph[x][y] = 0
    cnt = 1

    while dq:
        x, y = dq.popleft()

        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y

            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                dq.append((nx, ny))
                cnt += 1
    return cnt

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            result.append(bfs(graph, i, j))

result.sort()
print(len(result))
for i in range(len(result)):
    print(result[i])