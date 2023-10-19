from collections import deque

n, k, m = map(int, input().split())
li = [0] * n
tag = 1
cnt = 0

for i in range(n):
    li[i] = i + 1
q = deque(li)
flag = (-k + 1)

for i in range(n):
    if cnt//m > 0 and cnt%m == 0:
        flag = flag * (-1)
        tag = tag * (-1)
    q.rotate(flag)
    if tag == 1:
        print(q.popleft())
    else:
        print(q.pop())
    cnt += 1