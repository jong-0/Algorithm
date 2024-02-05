import sys
input = sys.stdin.readline

n = int(input())
li = [0] * n

for i in range(n):
    li[i] = int(input())
li.sort()

max = 0
for i in range(n):
    chk = li[i] * (n-i)
    if chk > max:
        max = chk

print(max)