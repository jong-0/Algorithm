h,m = map(int, input().split())
n = int(input())

if m+n < 60:
    print(h, m+n)
else:
    if (m+n)//60 + h > 23:
        print((h+(m+n)//60)%24, (m+n)%60)
    else:
        print(h+(m+n)//60, (m+n)%60)