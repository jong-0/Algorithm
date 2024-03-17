max = -1
cnt = 0
for _ in range(4):
    x, y = map(int, input().split())
    cnt += (y-x)
    if cnt > max:
        max = cnt
print(max)