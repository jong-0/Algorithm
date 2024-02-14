x, y, w, h = map(int, input().split())

x1 = w-x
x2 = x
y1 = h-y
y2 = y

print(min(x1,x2,y1,y2))