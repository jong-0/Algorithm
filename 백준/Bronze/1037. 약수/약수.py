import sys
input = sys.stdin.readline

n = int(input())
li = list(map(int,input().split()))
li.sort()

if len(li) == 1:
    print(li[0]**2)
else:
    print(li[0]*li[-1])