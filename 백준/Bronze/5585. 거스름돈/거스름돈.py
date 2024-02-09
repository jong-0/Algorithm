li = [500, 100, 50, 10, 5, 1]
n = int(input())
cnt = 0

n = 1000 - n

for i in li:
    if n//i > 0:
        cnt += n//i
        n = n - (n//i)*i

print(cnt)