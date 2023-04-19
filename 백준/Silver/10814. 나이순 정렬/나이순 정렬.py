import sys
input = sys.stdin.readline

n = int(input())
li = [0] * n

for i in range(n):
    li[i] = list(input().split())
li.sort(key=lambda x:int(x[0]))

for i in range(n):
    print(li[i][0], li[i][1])