n = int(input())
dict = {}
for _ in range(n):
    a,b = input().split('.')
    if b in dict:
        dict[b] += 1
    else:
        dict[b] = 1

di = sorted(dict)
for i in di:
    print(i, dict[i])