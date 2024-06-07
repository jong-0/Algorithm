n = int(input())
dict = {}
for _ in range(n):
    a,b = input().split('.')
    if b in dict:
        dict[b] += 1
    else:
        dict[b] = 1

dict = sorted(dict.items())

for i, j in dict:
    print(i, j)