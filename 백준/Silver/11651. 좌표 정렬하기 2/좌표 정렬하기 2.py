import sys
input = sys.stdin.readline

n = int(input())

li = [0] * n

for i in range(n):
    li[i] = list(map(int, input().split()))

li.sort()
li.sort(key=lambda x: x[1])

for i in range(n):
    print(li[i][0], li[i][1])