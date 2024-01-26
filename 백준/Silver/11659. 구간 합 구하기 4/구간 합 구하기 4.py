import sys
input = sys.stdin.readline

n,m = map(int, input().split())
li = list(map(int, input().rstrip().split()))

sum = [0] * len(li)
sum[0] = li[0]
for i in range(1, len(li)):
    sum[i] = sum[i-1] + li[i]
sum = [0] + sum

for _ in range(m):
    a,b = map(int, input().split())
    print(sum[b]-sum[a-1])