import sys
input = sys.stdin.readline

n = int(input())
li = list(map(int, input().rstrip().split()))
chk = list(map(int, input().rstrip().split()))

tag = 0
if li == chk:
    tag = 1
else:
    for i in range(n-1,0,-1):
        max_idx = i
        for j in range(i-1, -1, -1):
            if li[max_idx] < li[j]:
                max_idx = j

        if max_idx != i:
            li[max_idx], li[i] = li[i], li[max_idx]
            if li[i] == chk[i]:
                if li == chk:
                    tag = 1
                    break

if tag == 1:
    print(1)
else:
    print(0)