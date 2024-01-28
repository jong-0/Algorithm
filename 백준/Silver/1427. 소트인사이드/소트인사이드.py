import sys
input = sys.stdin.readline

s = list(input())
s.sort(reverse=True)
print(*s,sep='')