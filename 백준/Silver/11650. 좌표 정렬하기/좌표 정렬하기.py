import sys
input = sys.stdin.readline

n = int(input())
li = [0] * n

for i in range(n):
    li[i] = list(map(int, input().split()))

li.sort()

for i in range(n):
    print(*li[i])