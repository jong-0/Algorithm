s = 0
num = 100

for _ in range(7):
    n = int(input())
    if n%2 != 0:
        s += n
        if n < num:
            num = n

if s == 0:
    print(-1)
else:
    print(s)
    print(num)