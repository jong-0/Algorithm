num = int(input())
li=[0]*num

for i in range(num):
    li[i] = int(input())

li.sort()

for i in li:
    print(i)