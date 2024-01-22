li = [i for i in range(1,21)]

for _ in range(10):
    a, b = map(int, input().split())
    li[a-1:b] = li[a-1:b][::-1]

print(*li)