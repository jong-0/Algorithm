from collections import deque
import sys
input = sys.stdin.readline

q = deque()

n = int(input())
for i in range(n):
    a = input().split()

    if a[0] == 'back':
        if q:
            print(q[-1])
        else:
            print(-1)
    elif a[0] == 'front':
        if q:
            print(q[0])
        else:
            print(-1)
    elif a[0] == 'empty':
        if q:
            print(0)
        else:
            print(1)
    elif a[0] == 'size':
        print(len(q))
    elif a[0] == 'pop':
        if q:
            print(q.popleft())
        else:
            print(-1)
    else:
        q.append(a[1])