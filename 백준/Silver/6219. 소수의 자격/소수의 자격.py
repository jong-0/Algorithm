import math
a,b,d = map(int, input().split())

li = [True for i in range(b+1)]

for i in range(2, int(math.sqrt(b))+1):
    j = 2
    while i*j <= b:
        if li[i*j]:
            li[i*j] = False
        j += 1

ans = 0
for i in range(a, b+1):
    if i > 1:
        if li[i]:
            if str(d) in str(i):
                ans += 1

print(ans)