import sys
input = sys.stdin.readline

n, m = map(int, input().split())

li = [0] * n
for i in range(n):
    li[i] = i+1

for k in range(m):
    i, j = map(int, input().split())
    save = li[i-1]
    li[i-1] = li[j-1]
    li[j-1] = save

for i in li:
    print(i, end=' ')