li = list(map(int, input().split()))
li.sort()

if li[0] == li[1] == li[2]:
    print(li[0]*1000 + 10000)
elif li[0] == li[1] or li[1] == li[2]:
    print(1000 + li[1]*100)
else:
    print(li[2]*100)