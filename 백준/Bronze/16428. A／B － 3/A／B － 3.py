a, b = map(int, input().split())

if a > 0 > b:
    print(-(a//-b))
    print(a-(-(a//-b))*b)
elif a < 0 and b < 0:
    print(-(a//-b))
    print(a-(-(a//-b))*b)
else:
    print(a//b)
    print(a%b)