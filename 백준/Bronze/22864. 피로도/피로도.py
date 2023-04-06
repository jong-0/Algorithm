a,b,c,m = map(int, input().split())

work = 0
p = 0
t = 0

while True:
  if a > m:
    print(0)
    break
  
  else:
    if p + a > m:
      p -= c
      t +=1
      if p < 0:
        p = 0
    else:
      work += b
      p += a
      t += 1
    
    if t == 24:
      print(work)
      break