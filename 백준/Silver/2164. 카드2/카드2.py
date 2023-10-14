from collections import deque

n = int(input())
li = [0] * n

for i in range(n):
    li[i] = i + 1

q = deque(li)

while len(q) > 1:
    q.popleft()
    q.rotate(-1)

print(q[0])