sss = input()
num = int(input())

n = len(sss)
cnt = 0
for _ in range(num):
    s = input()
    s = s + s[:n - 1]
    if sss in s:
        cnt += 1

print(cnt)