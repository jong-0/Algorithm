n = int(input())
la = list(map(int, input().split()))
lb = list(map(int, input().split()))

la.sort()
lb.sort(reverse=True)

sum = 0
for i in range(n):
    sum += la[i]*lb[i]

print(sum)