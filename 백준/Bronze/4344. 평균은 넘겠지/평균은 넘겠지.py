n = int(input())
for _ in range(n):
    li = list(map(int, input().split()))
    num = li[0]
    total = sum(li[1:])
    avg = total // num
    cnt = 0

    for i in li[1:]:
        if i > avg:
            cnt += 1

    print("{:.3f}".format((cnt/num)*100)+'%')