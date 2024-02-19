abc = 'abcdefghijklmnopqrstuvwxyz'

n = int(input())
s = input()

ans = 0
for i in range(n):
    ans += (abc.index(s[i])+1) * 31**i

print(ans)