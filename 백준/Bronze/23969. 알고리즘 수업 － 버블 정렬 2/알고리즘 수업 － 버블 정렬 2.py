import sys
input = sys.stdin.readline

n, k = map(int, input().split())
li = list(map(int, input().split()))
cnt = 0

for i in range(n-1):
    tag = 1
    for j in range(n-i-1):
        if li[j] > li[j+1]:
            tag = -1
            cnt += 1
            li[j], li[j + 1] = li[j + 1], li[j]
            if cnt == k:
                print(*li)
                break
    if tag == 1:
        break

if cnt < k:
    print(-1)