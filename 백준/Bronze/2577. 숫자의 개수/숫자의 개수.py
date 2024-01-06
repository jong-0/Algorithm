li=[0]*10

n1 = int(input())
n2 = int(input())
n3 = int(input())

s = str(n1*n2*n3)

for i in s:
    li[int(i)] += 1

for i in li:
    print(i)