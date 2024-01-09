li = list(map(int, input().split()))

asc = sorted(li)
des = sorted(li, reverse=True)

if li == asc:
    print('ascending')
elif li == des:
    print('descending')
else:
    print('mixed')