li = list(map(int, input().split()))

li.sort()

if li[0] == li[2]:
    print(10000 + li[0]*1000)
elif li[1] == li[0] or li[1] == li[2]:
    print(1000 + li[1]*100)
else:
    print(li[2]*100)