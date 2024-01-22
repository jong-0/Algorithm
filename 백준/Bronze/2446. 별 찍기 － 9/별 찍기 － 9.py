n = int(input())
for i in range(n):
    print(' '*(i) + '*'*(2*(n-i)-1))

for i in range(1,n):
    print((n-1-i)*' ' + '*'*(2*(i+1)-1))