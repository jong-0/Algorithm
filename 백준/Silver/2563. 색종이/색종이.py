li = [[0]*101 for i in range(101)]

n = int(input())
for _ in range(n):
    x, y = map(int, input().split())
    for i in range(x, x+10):
        for j in range(y, y+10):
            li[i][j] = 1

sum = 0
for i in range(101):
    sum += li[i].count(1)
print(sum)