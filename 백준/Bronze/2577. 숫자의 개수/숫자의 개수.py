a = int(input())
b = int(input())
c = int(input())

s = str(a*b*c)

n = '0123456789'
li = [0] * 10

for i in s:
    if i in n:
        li[int(i)] += 1

print(*li, sep = '\n')