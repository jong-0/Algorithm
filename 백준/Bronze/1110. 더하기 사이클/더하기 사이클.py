n = int(input())
cnt = 0
start = n

while True:
    if n == 0:
        print(1)
        break
    else:
        if n < 10:
            n = int(str(n) + str(n))
            cnt += 1
        else:
            n = int(str(n%10) + str((n//10+n%10)%10))
            cnt += 1

        if n == start:
            print(cnt)
            break