n = int(input())
for _ in range(n):
    s = input().split()

    for i in range(len(s)):
        print(s[i][::-1], end =' ')