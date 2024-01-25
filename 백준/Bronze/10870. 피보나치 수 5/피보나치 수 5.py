li = [0] * 21

li[0] = 0
li[1] = 1

for i in range(2, 21):
    li[i] = li[i-1] + li[i-2]

n = int(input())
print(li[n])