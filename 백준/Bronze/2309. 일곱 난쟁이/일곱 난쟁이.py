import sys
input = sys.stdin.readline

li = []

for _ in range(9):
    n = int(input())
    li.append(n)

li.sort()
s = sum(li) - 100

i = 0
j = len(li) - 1

while li[i] + li[j] != s:
    if li[i] + li[j] > s:
        j -= 1
    else:
        i += 1

del li[j]
del li[i]

print(*li, sep='\n', end='')