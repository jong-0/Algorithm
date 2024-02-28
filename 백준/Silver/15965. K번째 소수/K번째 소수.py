num = int(input())
n = 10000000

li = [True] * (n+1)
ans = []

for i in range(2, n+1):
    if not li[i]:
        continue
    else:
        ans.append(i)
        for j in range(i+i, n+1, i):
            li[j] = False

print(ans[num-1])