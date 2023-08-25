import sys
input = sys.stdin.readline

n, k = map(int, input().split())

li = [[0,0,0,0,0,0],
    [0,0,0,0,0,0]]

for _ in range(n):
    s, g = map(int, input().split())
    li[s][g-1] += 1

sum = 0

for i in li[0]:
    if i == 0:
        continue
    elif i%k == 0:
        sum += i//k
    else:
        sum += (i//k+1)

for i in li[1]:
    if i == 0:
        continue
    elif i % k == 0:
        sum += i // k
    else:
        sum += (i // k + 1)

print(sum)