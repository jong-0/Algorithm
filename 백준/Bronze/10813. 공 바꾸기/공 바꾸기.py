n, m = map(int, input().split())
li = [i for i in range(1,n+1)]

for _ in range(m):
    a,b = map(int, input().split())
    aa = li[a-1]
    bb = li[b-1]
    li[a-1] = bb
    li[b-1] = aa

print(*li)