n = int(input())
li = list(map(int, input().split()))

if n == 1:
    print(li[0]**2)
else:
    print(min(li)*max(li))