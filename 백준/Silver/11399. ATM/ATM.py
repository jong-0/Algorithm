from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
li = list(map(int, input().rstrip().split()))
li.sort()

for i in range(1, n):
    li[i] = li[i] + li[i-1]

print(sum(li))