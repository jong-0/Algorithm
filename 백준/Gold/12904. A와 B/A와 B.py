check = input()
s = input()

while True:
  if s[-1] == 'A':
    s = s[:len(s) - 1]
  elif s[-1] == 'B':
    s = s[:len(s) - 1]
    s = s[::-1]
  
  if s == check:
    print(1)
    break
  
  if len(s)==0:
    print(0)
    break