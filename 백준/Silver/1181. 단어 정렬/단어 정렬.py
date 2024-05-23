n = int(input())
li = []
for _ in range(n):
    li.append(input())

li = list(set(li))
li.sort()
li.sort(key=len)
print(*li, sep='\n')