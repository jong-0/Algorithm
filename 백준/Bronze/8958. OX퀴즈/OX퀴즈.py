num = int(input())
for i in range(num):
    s = input()
    cnt = 1
    sum = 0
    for j in s:
        if j =='O':
            sum += cnt
            cnt += 1
        else:
            cnt = 1
            continue
    print(sum)