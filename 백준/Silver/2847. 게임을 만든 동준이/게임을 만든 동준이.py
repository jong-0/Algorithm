import sys
input = sys.stdin.readline

n = int(input())
li = [0] * n

for i in range(n):
    li[n-i-1] = int(input())

ans = 0
for i in range(1, n):
    if li[i] >= li[i-1]:
        cnt = li[i-1] - 1
        ans += li[i] - cnt
        li[i] = cnt

print(ans)