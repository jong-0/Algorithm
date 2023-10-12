import sys
input = sys.stdin.readline

num = int(input())

li = []
ans = []
ii = 1
cnt = 0

for _ in range(num):
    n = int(input())

    while ii <= n:
        li.append(ii)
        ans.append('+')
        ii += 1

    if li[-1] == n:
        li.pop()
        ans.append('-')
    else:
        print('NO')
        cnt = 1
        break
if cnt == 0:
    print(*ans, sep='\n', end='')