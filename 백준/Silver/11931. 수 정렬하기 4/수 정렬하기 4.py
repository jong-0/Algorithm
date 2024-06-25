import sys
input = sys.stdin.readline

n = int(input())
li = [0] * n
for i in range(n):
    li[i] = int(input().rstrip())

li.sort(reverse=True)
print(*li, sep="\n")