n = int(input())
li = [0] * n

for i in range(n):
    li[i] = input()

sor = sorted(li)
rev = sorted(li, reverse=True)

if li == sor:
    print('INCREASING')
elif li == rev:
    print('DECREASING')
else:
    print('NEITHER')