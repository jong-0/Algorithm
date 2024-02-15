import sys
input = sys.stdin.readline

n, k = map(int, input().split())
li = list(map(int, input().rstrip().split()))

cnt = 0
for i in range(n-1, 0, -1):
    max_idx = i
    for j in range(i-1, -1, -1):
        if li[max_idx] < li[j]:
            max_idx = j

    if max_idx != i:
        li[max_idx], li[i] = li[i], li[max_idx]
        cnt += 1

    if cnt == k:
        print(li[max_idx], li[i])
        break
        
if cnt < k:
    print(-1)