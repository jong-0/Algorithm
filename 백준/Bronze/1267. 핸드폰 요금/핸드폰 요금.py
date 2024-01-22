n = int(input())
li = list(map(int,input().split()))
y, m = 0, 0

for i in range(len(li)):
    y += (li[i]//30 + 1) * 10
    m += (li[i]//60 + 1) * 15

if y == m:
    print('Y', 'M', y)
elif y < m:
    print('Y', y)
else:
    print('M', m)