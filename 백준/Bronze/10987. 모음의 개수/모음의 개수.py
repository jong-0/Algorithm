li = ['a','e','i','o','u']
s = input()
ans = 0
for i in s:
    if i in li:
        ans += 1
        
print(ans)