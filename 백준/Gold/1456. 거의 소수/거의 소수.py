import sys
input = sys.stdin.readline

n, k = map(int, input().split())
li = [True] * (int(k ** 0.5)+1)

for i in range(2, int(k ** 0.5)+1):
    if not li[i]:
        continue
    for j in range(i+i, int(k ** 0.5)+1, i):
        li[j] = False

cnt = 0
for i in range(2, len(li)):
    j = 2
    if li[i]:
        while i ** j <= k:
            if i ** j >= n:
                cnt += 1
            j += 1

print(cnt)