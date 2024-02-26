import math
n = 123456
li = [True for i in range(2*n+1)]

for i in range(2, int(math.sqrt(2 * n))+1):
    j = 2
    while i*j <= 2*n:
        li[i*j] = False
        j += 1

while True:
    start = int(input())
    end = start * 2

    if start == 0:
        break
    else:
        cnt = 0
        for i in range(start+1, end+1):
            if i < 2:
                continue
            else:
                if li[i]:
                    cnt += 1
        print(cnt)