import sys
input = sys.stdin.readline

num = int(input())
n = 0
li = []

for _ in range(num):
    cc = int(input())

    if cc == 0:
        li.pop()
    else:
        li.append(cc)

print(sum(li))