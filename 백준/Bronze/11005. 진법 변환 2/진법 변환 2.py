from collections import deque

li = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
s, n = map(int, input().split())
ans = deque()

while True:
    if s >= n:
        ans.appendleft(li[s%n])
        s = s//n
    else:
        ans.appendleft(li[s])
        break

print(*ans, sep='')