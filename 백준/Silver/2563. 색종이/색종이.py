num = int(input())
li = [[0 for j in range(100)] for _ in range(100)]
cnt = 0

for _ in range(num):
    x, y = map(int, input().split())
    for i in range(x,x+10):
        for j in range(y, y+10):
            if li[i][j] == 0:
                li[i][j] = 1
                cnt += 1
            else:
                continue

print(cnt)