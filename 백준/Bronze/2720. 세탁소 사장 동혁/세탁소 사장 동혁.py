li = [25, 10, 5, 1]

num = int(input())
for _ in range(num):
    n = int(input())
    for i in li:
        if n//i > 0:
            print(n//i, end=' ')
            n = n - (n//i)*i
        else:
            print(0, end=' ')