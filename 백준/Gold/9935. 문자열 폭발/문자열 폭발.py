import sys
input = sys.stdin.readline

li = list(input().rstrip())
chk = list(input().rstrip())
length = len(chk)
ans = []

for i in li:
    ans.append(i)
    if ans[-length:] == chk:
        for _ in range(length):
            ans.pop()

if ans:
    print(*ans, sep='')
else:
    print("FRULA")