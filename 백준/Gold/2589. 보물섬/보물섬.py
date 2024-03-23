import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
graph = []
result = []
for _ in range(n):
    graph.append(list(input()))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def bfs(x, y):
    dq = deque()
    dq.append((x, y))
    cnt = 0
    chk = [[-1] * m for _ in range(n)]
    chk[x][y] = cnt

    while dq:
        x, y = dq.popleft()
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y

            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if graph[nx][ny] == 'L' and chk[nx][ny] == -1:
                chk[nx][ny] = chk[x][y] + 1
                dq.append((nx, ny))
                cnt = max(cnt, chk[nx][ny])
    return cnt

for i in range(n):
    for j in range(m):
        if graph[i][j] == 'L':
            result.append(bfs(i, j))

print(max(result))