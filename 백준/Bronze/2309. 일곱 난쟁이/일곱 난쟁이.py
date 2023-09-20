import sys
input = sys.stdin.readline

li=[0] * 9
for i in range(9):
    li[i] = int(input())

li.sort()
n = sum(li) - 100

for i in range(len(li) - 1):
    for j in range(i + 1, len(li)):
        if li[i] + li[j] == n:
            li.remove(li[j])
            li.remove(li[i])
            break
    if len(li) < 9:
        break
        
print(*li, sep='\n')