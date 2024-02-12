import sys
input = sys.stdin.readline

n, k = map(int, input().split())
li = list(map(int, input().split()))
cnt = 0

for i in range(n-1):
    tag = 1
    for j in range(0, n-i-1):
        if li[j] > li[j+1]:
            cnt += 1
            if cnt == k:
                print(li[j+1], li[j])
                break
            li[j], li[j+1] = li[j+1], li[j]
            tag = -1
    if tag == 1:
        break
if cnt < k:
    print(-1)