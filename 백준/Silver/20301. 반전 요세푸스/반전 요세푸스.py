from collections import deque
import sys
input = sys.stdin.readline

n, k, m = map(int, input().split())
dq = deque(i for i in range(1,n+1))

cnt = 0
chk = 0
tag = 1
while dq:
    cnt += 1
    if chk > 0 and chk%m == 0:
        tag *= (-1)
        chk = 0

    if tag == 1:
        if cnt % k == 0:
            print(dq.popleft())
            chk += 1
        else:
            dq.append(dq.popleft())
    else:
        if cnt % k == 0:
            print(dq.pop())
            chk += 1
        else:
            dq.appendleft(dq.pop())