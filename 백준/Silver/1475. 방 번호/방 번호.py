import math

li1 ='0123456789'
li1 = list(li1)
li=[0,0,0,0,0,0,0,0,0,0]

n=list(input())
for i in n:
  if i in li1:
    li[int(i)]+=1

li69=[]
li69.append(li[6])
li69.append(li[9])
del li[9]
del li[6]

lis=[]
lis.append(max(li))
lis.append(math.ceil(sum(li69)/2))
print(max(lis))