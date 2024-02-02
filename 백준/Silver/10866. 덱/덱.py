from collections import deque
import sys
input = sys.stdin.readline

dq = deque()
n = int(input())
for _ in range(n):
    s = input().split()
    if s[0] == 'push_back':
        dq.append(s[-1])
    elif s[0] == 'push_front':
        dq.appendleft(s[-1])
    elif s[0] == 'pop_front':
        if len(dq) > 0:
            print(dq.popleft())
        else:
            print(-1)
    elif s[0] == 'pop_back':
        if len(dq) > 0:
            print(dq.pop())
        else:
            print(-1)
    elif s[0] == 'size':
        print(len(dq))
    elif s[0] == 'empty':
        if len(dq) > 0:
            print(0)
        else:
            print(1)
    elif s[0] == 'front':
        if len(dq) > 0:
            print(dq[0])
        else:
            print(-1)
    else:
        if len(dq) > 0:
            print(dq[-1])
        else:
            print(-1)