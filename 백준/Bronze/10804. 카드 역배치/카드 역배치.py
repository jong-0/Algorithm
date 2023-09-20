import sys
input = sys.stdin.readline

li = [0] * 20
for i in range(20):
    li[i] = i+1

for _ in range(10):
    a, b = map(int, input().split())
    if a == b:
        continue
    else:
        if a == 1:
            li[a-1:b] = li[b-1::-1]
        else:
            li[a-1:b] = li[b-1:a-2:-1]

print(*li)