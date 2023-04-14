n, m = map(int, input().split())
li = list(map(int, input().split()))

ans = 0

for i in range(n):
    for j in range(n-2):
        for k in range(j+1, n-1):
            for l in range(k+1, n):
                sum = li[j] + li[k] + li[l]
                if sum <= m and sum > ans:
                    ans = sum
                else:
                    continue
print(ans)