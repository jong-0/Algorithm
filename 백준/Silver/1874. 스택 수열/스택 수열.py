import sys
input = sys.stdin.readline

num = int(input())

li = []
ans = []
i = 1
tag = 0

for _ in range(num):
    n = int(input())

    while i <= n:
        li.append(i)
        ans.append('+')
        i += 1

    if li[-1] == n:
        li.pop()
        ans.append('-')
    else:
        tag = 1
        break

if tag == 0:
    print(*ans, sep='\n', end='')
else:
    print('NO')