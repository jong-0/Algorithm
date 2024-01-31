import sys
input = sys.stdin.readline

n, m = map(int, input().split())
li = [0] + list(map(int, input().rstrip().split()))

chk = [0] * (n-m+1)

for i in range(1, n+1):
    li[i] = li[i-1] + li[i]

for i in range(len(chk)):
    chk[i] = li[m+i] - li[i]

max = max(chk)
if max == 0:
    print('SAD')
else:
    print(max)
    print(chk.count(max))