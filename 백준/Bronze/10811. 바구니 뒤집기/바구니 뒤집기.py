import sys
input = sys.stdin.readline

n, m = map(int, input().split())

li = [0] * n

for i in range(n):
    li[i] = i+1

for i in range(m):
    a, b = map(int, input().split())
    if a == 1:
        li[a-1:b] = li[b-1::-1]
    else:
        li[a-1:b] = li[b-1:a-2:-1]

for i in li:
    print(i, end = ' ')