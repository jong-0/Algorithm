n = int(input())
s = input()

ans = 0
for i in range(n):
    ans += (ord(s[i])-96) * 31**i

print(ans % 1234567891)