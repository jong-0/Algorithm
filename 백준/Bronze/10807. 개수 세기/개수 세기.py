n = int(input())
li = list(map(int, input().split()))
chk = int(input())

ans = 0

for i in li:
    if i == chk:
        ans += 1

print(ans)