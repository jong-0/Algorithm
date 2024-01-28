n, m = map(int, input().split())
li = list(map(int, input().split()))
li.sort(reverse=True)
print(li[m-1])