max = 0
idx = 0
cnt = 0

for i in range(1,10):
    n = int(input())
    cnt += 1
    if n > max:
        max = n
        idx = cnt

print(max)
print(idx)