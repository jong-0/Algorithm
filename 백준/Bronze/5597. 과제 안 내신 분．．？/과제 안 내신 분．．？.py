li = [0] * 30
for i in range(30):
    li[i] = i+1

for i in range(28):
    n = int(input())
    li.remove(n)

print(*li, sep='\n')