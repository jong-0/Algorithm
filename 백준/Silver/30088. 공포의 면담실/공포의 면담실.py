import sys
input = sys.stdin.readline

n = int(input())
chk = [0] * n
for i in range(n):
    li = list(map(int, input().rstrip().split()))
    li[0] = 0
    for j in range(1,len(li)):
        li[j] = li[j] + li[j-1]
    chk[i] = li[-1]

chk.sort()
for i in range(1, len(chk)):
    chk[i] = chk[i] + chk[i-1]
print(sum(chk))