n, c = map(int, input().split())
li = list(map(int, input().split()))

for i in li:
    if i < c:
        print(i, end=' ')