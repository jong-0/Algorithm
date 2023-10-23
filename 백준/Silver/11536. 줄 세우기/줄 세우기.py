import sys
input= sys.stdin.readline

num = int(input())
li = [0] * num

for i in range(num):
    li[i] = input()

inc = sorted(li)
dec = sorted(li, reverse=True)

if li == inc:
    print('INCREASING')
elif li == dec:
    print('DECREASING')
else:
    print('NEITHER')