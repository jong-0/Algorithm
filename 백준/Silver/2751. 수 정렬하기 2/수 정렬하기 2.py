import sys
input = sys.stdin.readline

num = int(input())
li = [0] * num
for i in range(num):
    li[i] = int(input())

li.sort()
print(*li, sep='\n')