from collections import deque

def bfs(graph, x, y):
    dx = [-1, 1, 0, 0, -1, 1, -1, 1]
    dy = [0, 0, -1, 1, -1, -1, 1, 1]
    dq = deque()
    dq.append((x, y))
    graph[x][y] = 0
    cnt = 1

    while dq:
        x, y = dq.popleft()
        for i in range(8):
            nx = dx[i] + x
            ny = dy[i] + y

            if nx < 0 or ny < 0 or nx >= h or ny >= w:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                dq.append((nx, ny))
    return cnt

while True:
    w, h = map(int, input().split())
    graph = []
    result = 0
    if w == 0 and h == 0:
        break
    else:
        for _ in range(h):
            graph.append(list(map(int, input().split())))

        for i in range(w):
            for j in range(h):
                if graph[j][i] == 1:
                    result += bfs(graph, j, i)
    print(result)