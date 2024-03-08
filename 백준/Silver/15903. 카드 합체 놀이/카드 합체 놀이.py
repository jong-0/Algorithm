import sys
input = sys.stdin.readline

n, k = map(int, input().split())
li = list(map(int, input().rstrip().split()))

for _ in range(k):
    li.sort()
    su = li[0] + li[1]
    li[0], li[1] = su, su

print(sum(li))