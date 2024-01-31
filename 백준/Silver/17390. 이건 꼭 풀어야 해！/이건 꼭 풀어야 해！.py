import sys
input = sys.stdin.readline

n, q = map(int, input().split())
li = [0] + list(map(int, input().rstrip().split()))
li.sort()

for i in range(1, n+1):
    li[i] = li[i-1] + li[i]

for _ in range(q):
    i, j = map(int, input().split())
    print(li[j]-li[i-1])