num = 0
s = 0
for i in range(1,10):
    n = int(input())
    if n > s:
        s = n
        num = i

print(s)
print(num)