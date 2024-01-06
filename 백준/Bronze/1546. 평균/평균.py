num = int(input())
li = list(map(int, input().split()))
li.sort()

max = li[-1]
sum = 0

for i in range(num):
    sum += li[i]/max*100

print(sum/num)