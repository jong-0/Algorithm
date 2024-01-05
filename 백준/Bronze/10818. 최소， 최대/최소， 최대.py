import sys
input = sys.stdin.readline

num = int(input())
li = list(map(int, input().strip().split()))

max = -1000001
min = 1000001

for i in range(num):
    if li[i] > max:
        max = li[i]

    if li[i] < min:
        min = li[i]

print(min, max)