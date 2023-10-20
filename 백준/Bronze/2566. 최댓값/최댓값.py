import sys

li = []
max = 0
ii = 1
jj = 1

for i in range(9):
    li.append(list(map(int, sys.stdin.readline().rstrip().split())))

for i in range(9):
    for j in range(9):
        if li[i][j] > max:
            max = li[i][j]
            ii = i+1
            jj = j+1

print(max)
print(ii, jj)