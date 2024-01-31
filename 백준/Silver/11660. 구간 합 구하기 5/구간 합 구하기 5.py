import sys
input = sys.stdin.readline

n, m = map(int, input().split())
li = [[0] * (n+1)]
for i in range(1, n+1):
    li.append([0] + list(map(int, input().rstrip().split())))

chk = [[0]*(n+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, n+1):
        if i == 1 and j == 1:
            chk[i][j] = li[1][1]
        elif i == 1 and j > 1:
            chk[i][j] = chk[i][j-1] + li[i][j]
        elif i > 1 and j == 1:
            chk[i][j] = chk[i-1][j] + li[i][j]
        else:
            chk[i][j] = chk[i-1][j] + chk[i][j-1] - chk[i-1][j-1] + li[i][j]

for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    print(chk[x2][y2] - chk[x1-1][y2] - chk[x2][y1-1] + chk[x1-1][y1-1])