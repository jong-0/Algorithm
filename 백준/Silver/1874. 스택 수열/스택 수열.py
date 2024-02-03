from collections import deque
import sys
input = sys.stdin.readline

num = int(input())
li = deque([i for i in range(1, num+1)])
dq = deque()
ans = []
tag = 0

for _ in range(num):
    n = int(input())
    while tag == 0:
        if len(dq) == 0:
            dq.append(li.popleft())
            ans.append('+')
        else:
            if dq[-1] != n:
                if len(li) != 0:
                    dq.append(li.popleft())
                    ans.append('+')
                else:
                    tag = 1
            else:
                dq.pop()
                ans.append('-')
                break

if tag == 1:
    print('NO')
else:
    print(*ans, sep='\n')