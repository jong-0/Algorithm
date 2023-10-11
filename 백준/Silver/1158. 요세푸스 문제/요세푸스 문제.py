import sys
input = sys.stdin.readline

from collections import deque

q = deque()

n, k =map(int, input().split())
cnt = 0
li = []

for i in range(1,n+1):
    q.append(i)

while len(q) != 0:
    q.rotate(-k+1)
    li.append(q.popleft())

print('<', end='')
print(*li, sep=', ', end='')
print('>', end='')