li = []
ans = []
cnt = 0
for i in range(1, 9):
    n = int(input())
    li.append([n, i])

li.sort(reverse = True)

for i in range(5):
    ans.append(li[i][1])
    cnt += li[i][0]

ans.sort()

print(cnt)
print(*ans)