n = int(input())
for i in range(1,n+1):
    print('*'*i + ' '*(2*n-2*i) + '*'*i)

for i in range(1,n):
    print('*'*(n-i) + ' '*(i*2) + '*'*(n-i))