li = list(map(int, input().split()))
li.sort()

if li[0] == li[1] and li[1] == li[2] and li[2] == li[0]:
    print(li[0]*3)
else:
    if li[0] + li[1] > li[2]:
        print(sum(li))
    else:
        print((li[0]+li[1])*2 - 1)