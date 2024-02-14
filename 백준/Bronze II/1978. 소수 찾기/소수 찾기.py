n = int(input())
li = list(map(int, input().split()))

cnt = 0

for i in li:
    tag = 1
    if i == 1:
        continue
    else:
        for j in range(2,i):
            if i%j == 0:
                tag = 0
                break
        if tag == 1:
            cnt += 1

print(cnt)
