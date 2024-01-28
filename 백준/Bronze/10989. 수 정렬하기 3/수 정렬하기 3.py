import sys
input = sys.stdin.readline

li = [0] * 10001
num = int(input())
for _ in range(num):
    n = int(input())
    li[n] += 1

for i in range(1,len(li)):
    if li[i] != 0:
        for j in range(li[i]):
            print(i)