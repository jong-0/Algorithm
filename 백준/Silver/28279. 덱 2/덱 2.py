from collections import deque
import sys
input = sys.stdin.readline

dq = deque()
n = int(input())
for _ in range(n):
    s = input().split()
    if s[0] == '1':
        dq.appendleft(int(s[-1]))
    elif s[0] == '2':
        dq.append(int(s[-1]))
    elif s[0] == '3':
        if len(dq) > 0:
            print(dq.popleft())
        else:
            print(-1)
    elif s[0] == '4':
        if len(dq) > 0:
            print(dq.pop())
        else:
            print(-1)
    elif s[0] == '5':
        print(len(dq))
    elif s[0] == '6':
        if len(dq) > 0:
            print(0)
        else:
            print(1)
    elif s[0] == '7':
        if len(dq) > 0:
            print(dq[0])
        else:
            print(-1)
    else:
        if len(dq) > 0:
            print(dq[-1])
        else:
            print(-1)