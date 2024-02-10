start = 2
n = int(input())
cnt = 0

while cnt != n:
    start = start + (start-1)
    cnt += 1

print(start**2)