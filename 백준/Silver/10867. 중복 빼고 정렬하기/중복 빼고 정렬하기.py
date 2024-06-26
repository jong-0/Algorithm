n = int(input())
li = list(map(int, input().split()))
li = list(set(li))
li.sort()

print(*li, sep=' ')