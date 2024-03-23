from collections import deque
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

            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                dq.append((nx, ny))
    return cnt


tc = int(input())
for _ in range(tc):
    result = 0
    m, n, k = map(int, input().split())
    graph = [[0]*m for _ in range(n)]
    for _ in range(k):
        x, y = map(int, input().split())
        graph[y][x] = 1

    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                result += bfs(graph, i, j)

    print(result)