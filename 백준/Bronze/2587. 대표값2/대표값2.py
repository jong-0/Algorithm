li = [0] * 5
sum = 0
for i in range(5):
    n = int(input())
    sum += n
    li[i] = n

li.sort()
print(int(sum/5))
print(li[2])