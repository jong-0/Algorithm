import sys
input = sys.stdin.readline

from collections import deque
dq = deque()

n = int(input())

for _ in range(n):
    s = list(input().split())
    if 'push_back' == s[0]:
        dq.append(s[-1])
    elif 'push_front' in s:
        dq.appendleft(s[-1])
    elif s[0] == 'front':
        if len(dq) == 0:
            print(-1)
        else:
            print(dq[0])
    elif s[0] == 'back':
        if len(dq) == 0:
            print(-1)
        else:
            print(dq[-1])
    elif s[0] == 'empty':
        if len(dq) == 0:
            print(1)
        else:
            print(0)
    elif s[0] == 'pop_front':
        if len(dq) == 0:
            print(-1)
        else:
            print(dq.popleft())
    elif s[0] == 'pop_back':
        if len(dq) == 0:
            print(-1)
        else:
            print(dq.pop())
    elif s[0] == 'size':
        print(len(dq))