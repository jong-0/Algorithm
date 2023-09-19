a,b = map(int,input().split())

A = min(a,b)
B = max(a,b)
li=[]

if B<=A:
    print(0)
else:
    n = B-A-1
    for i in range(A+1,B):
        li.append(i)
    
    print(n)
    print(*li)