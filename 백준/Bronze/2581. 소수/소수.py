m = int(input())
n = int(input())

li = [True] * (n+1)

for i in range(2, n+1):
    if not li[i]:
        continue
    for j in range(i+i, n+1, i):
        li[j] = False

ans = 0
min = 0
for i in range(m, n+1):
    if i > 1:
        if li[i]:
            if min == 0:
                min = i
            ans += i

if ans == 0:
    print(-1)
else:
    print(ans)
    print(min)