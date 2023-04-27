n , m = map(int, (input().split()))
li = [0] * n

for _ in range(m):
    i, j, k = map(int, input().split())
    for a in range(i-1,j):
        li[a] = k
li = map(str, li)
print(' '.join(li))