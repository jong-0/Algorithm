cnt = 0
n = int(input())

if n == 1:
    print(1)
else:
    for i in range(1, n):
        n -= 6*i
        cnt += 1
        if n <= 1:
            break

    print(cnt+1)