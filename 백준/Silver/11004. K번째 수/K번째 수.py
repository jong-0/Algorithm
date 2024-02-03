import sys
input = sys.stdin.readline

n, m = map(int, input().split())
li = list(map(int, input().rstrip().split()))
li.sort()

print(li[m-1])