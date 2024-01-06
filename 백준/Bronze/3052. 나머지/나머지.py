li = [0]*10
for i in range(10):
    li[i] = int(input())%42

print(len(set(li)))