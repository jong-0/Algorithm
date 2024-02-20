import sys
input = sys.stdin.readline

num = int(input())
for _ in range(num):
    j, n = map(int,input().split())
    li = [0] * n
    for i in range(n):
        r, c = map(int, input().split())
        li[i] = r*c

    li.sort(reverse=True)
    cnt = 0
    for k in li:
        j -= k
        cnt += 1
        if j <= 0:
            break
    print(cnt)