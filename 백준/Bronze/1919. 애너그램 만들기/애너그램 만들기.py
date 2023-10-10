import sys
input = sys.stdin.readline

a = list(input())
b = list(input())

s = 0

i = 0

while i < len(a):
    if a[i] in b:
        b.remove(a[i])
        a.remove(a[i])
    else:
        i+=1

print(len(a) + len(b))