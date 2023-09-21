import sys
input = sys.stdin.readline

num = int(input())
li = list(map(int, input().split()))
n = int(input())

s = 0

for i in li:
    if n == i:
        s+=1

print(s)