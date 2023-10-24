num = int(input())
for i in range(1, num+1):
    s = input()
    cnt = 1
    for j in range(len(s)):
        while s[:cnt] != s[cnt:cnt+cnt]:
            cnt+=1
    print('#'+str(i), cnt)