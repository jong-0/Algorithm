from collections import deque
import sys
input = sys.stdin.readline

dq = deque()

num = int(input())
for _ in range(num):
    n = int(input())
    if n == 0:
        dq.pop()
    else:
        dq.append(n)

print(sum(dq))