from collections import deque

num = int(input())
li = list(map(int, input().split()))
q = deque()

for i in range(num):
    q.append(i+1)

ans = []

for i in range(num):
    ans.append(q.popleft())
    chk = li[ans[-1]-1]
    if chk > 0:
        q.rotate(1-li[ans[-1]-1])
    else:
        q.rotate(-li[ans[-1]-1])

print(*ans, end='')