import math
n, m = map(int, input().split())

li = [True for i in range(m+1)]

for i in range(2, int(math.sqrt(m))+1):
    if li[i] == True:
        j = 2
        while i * j <= m:
            li[i*j] = False
            j += 1

for i in range(n, m+1):
    if i < 2:
        continue
    else:
        if li[i]:
            print(i)