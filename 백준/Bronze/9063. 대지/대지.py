n = int(input())
lx = [0] * n
ly = [0] * n

for i in range(n):
    x, y = map(int, input().split())
    lx[i] = x
    ly[i] = y

if n == 1:
    print(0)
else:
    print((max(lx)-min(lx)) * (max(ly)-min(ly)))