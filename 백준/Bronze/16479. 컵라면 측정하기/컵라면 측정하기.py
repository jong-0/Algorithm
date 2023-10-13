k = float(input())
li = list(map(float, input().split()))

li.sort()

print(k**2 - ((li[1]-li[0])/2) ** 2)