n, m = map(int, input().split())
li = list(map(int, input().split()))

for i in li:
    if i < m:
        print(i, end=' ')