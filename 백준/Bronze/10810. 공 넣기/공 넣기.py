n, m = map(int, input().split())
li = [0 for _ in range(n)]

for _ in range(m):
    i, j, k = map(int, input().split())
    li[i-1:j] = [k] * (j-i+1)

print(*li)