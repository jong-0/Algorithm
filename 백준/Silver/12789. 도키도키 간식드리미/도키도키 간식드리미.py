from collections import deque

n = int(input())
dq = deque(map(int, input().split()))
ans = [0]
chk = []

for i in range(n):
    chk.append(dq.popleft())
    while True:
        if len(chk) == 0:
            break
        else:
            if ans[-1] + 1 == chk[-1]:
                ans.append(chk.pop())
            else:
                break

if len(ans) == n+1:
    print('Nice')
else:
    print('Sad')