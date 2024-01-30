n, k = map(int, input().split())
li = list(map(int, input().split()))

for i in range(n-k+1):
    li[i] = sum(li[i:i+k])

for i in range(k-1):
    li.pop()
print(max(li))