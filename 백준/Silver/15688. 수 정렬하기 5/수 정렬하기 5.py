import sys
input = sys.stdin.readline

num = int(input())
li = []

for i in range(num):
    li.append(int(input()))

li.sort()

print(*li, sep='\n')