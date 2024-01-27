n, k = map(int, input().split())
li = list(map(int, input().split()))

for i in range(1, len(li)):
    li[i] = li[i] + li[i-1]

li.sort(reverse=True)
print(sum(li[:k]))