li1 = list(map(int, input().split()))
li2 = list(map(int, input().split()))

mg = sum(li1)
ms = sum(li2)

if mg == ms:
    print(mg)
else:
    print(max(mg, ms))