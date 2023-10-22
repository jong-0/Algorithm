#li = [[0] * 1000 for i in range(1000)]
bx, by = map(int,input().split())
dx, dy = map(int,input().split())
jx, jy = map(int,input().split())

b = 0
d = 0

d += (abs(jx-dx))
d += (abs(jy-dy))

b += (max(abs(jx-bx), abs(jy-by)))

if d > b:
    print('bessie')
elif b > d:
    print('daisy')
else:
    print('tie')