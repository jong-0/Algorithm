from collections import deque
import sys
input = sys.stdin.readline

dq = deque()
n = int(input())

for i in range(n):
    dq.append(n-i)

while len(dq) != 1:
    dq.pop()
    dq.appendleft(dq.pop())

print(dq[0])