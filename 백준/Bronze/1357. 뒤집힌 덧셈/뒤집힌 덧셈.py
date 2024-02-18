a,b = input().split()
a = a[::-1]
b = b[::-1]

ans = str(int(a) + int(b))[::-1]
print(int(ans))