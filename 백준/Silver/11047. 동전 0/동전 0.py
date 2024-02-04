import sys
input = sys.stdin.readline

n, k = map(int, input().split())
li = [0] * n
for i in range(n):
    li[n-1-i] = int(input())

cnt = 0
idx = 0
while k != 0:
    if k//li[idx] > 0:
        cnt += k // li[idx]
        k = k - (k//li[idx])*li[idx]
        idx += 1
    else:
        idx += 1

print(cnt)