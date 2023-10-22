n, m, k = map(int, input().split())
li = [i for i in range(1, n+1)]

print(li[(m+k-4)%n])