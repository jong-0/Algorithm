import math
n, k = map(int, input().split())

li = [True for i in range(n+1)]

cnt = 0
for i in range(2, n+1):
    j = 1
    while i*j <= n:
        if li[i*j]:
            li[i*j] = False
            cnt += 1
            if cnt == k:
                print(i*j)
                break
        j += 1