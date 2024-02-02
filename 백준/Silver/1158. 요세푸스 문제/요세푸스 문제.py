from collections import deque
import sys
input = sys.stdin.readline

dq = deque()
n, m = map(int, input().split())

for i in range(1,n+1):
    dq.append(i)

ans = []
cnt = 0
while len(dq) != 0:
    cnt += 1
    if cnt%m == 0:
        ans.append(dq.popleft())
    else:
        dq.append(dq.popleft())

print('<', end='')
print(*ans, sep=', ', end='')
print('>')