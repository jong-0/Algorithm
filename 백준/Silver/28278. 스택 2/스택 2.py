from collections import deque
import sys
input = sys.stdin.readline

dq = deque()
n = int(input())
for _ in range(n):
    s = input().split()
    if s[0] == '1':
        dq.append(int(s[-1]))
    elif s[0] == '2':
        if len(dq) > 0:
            print(dq.pop())
        else:
            print(-1)
    elif s[0] == '3':
        print(len(dq))
    elif s[0] == '4':
        if len(dq) > 0:
            print(0)
        else:
            print(1)
    else:
        if len(dq) > 0:
            print(dq[-1])
        else:
            print(-1)