n, m = map(int, input().split())
li = list(map(int, input().split()))

ans = 0
min = m
for i in range(n-2):
    for j in range(i+1, n-1):
        for k in range(j+1, n):
            if abs(m-(li[i] + li[j] + li[k])) < min and (li[i] + li[j] + li[k]) <= m:
                min = abs(m-(li[i] + li[j] + li[k]))
                ans = (li[i] + li[j] + li[k])

print(ans)