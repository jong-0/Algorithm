from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
li = list(map(int, sys.stdin.readline().rstrip().split()))
lid = [0] * n

for i in range(n):
    lid[i] = i + 1

q = deque(lid)
cnt = 0

for i in range(m):
    r = 0
    l = 0
    idx = 0

    idx = q.index(li[i])
    if idx == 0:
        q.popleft()
        continue
    else:
        r = q.index(li[i])
        l = len(q) - q.index(li[i])

        if r > l:
            q.rotate(l)
            cnt += l
            q.popleft()
        else:
            q.rotate(-r)
            cnt += r
            q.popleft()

print(cnt)