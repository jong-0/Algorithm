n, m = map(int, input().split())
a = min(n, m)
b = max(n, m)
li = [i for i in range(a+1,b)]

print(len(li))
print(*li)