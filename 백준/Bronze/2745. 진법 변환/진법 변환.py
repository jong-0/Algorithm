li = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
s, n = input().split()
sum = 0

for i in range(len(s)):
    sum += li.index(s[i]) * int(n)**(len(s)-1-i)

print(sum)