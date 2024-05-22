import sys
input = sys.stdin.readline

n, m = map(int, input().split())

de = set()
bo = set()

for i in range(n):
   de.add(input().rstrip()) 

for j in range(m):
    bo.add(input().rstrip())

ans = list(de & bo)
ans.sort()

print(len(ans))
print(*ans, sep='\n')