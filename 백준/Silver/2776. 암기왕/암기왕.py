def binary_search(target, data):
  start = 0
  end = len(data) - 1

  while start <= end:
    mid = (start + end) // 2
    if data[mid] == target:
      return 1
    elif data[mid] < target:
      start = mid + 1
    else:
      end = mid - 1
  
  return 0

t = int(input())
for j in range(t):
  n1 = int(input())
  data = list(map(int, input().split()))
  data.sort()

  n2 = int(input())
  target = list(map(int, input().split()))


  for i in range(n2):
    print(binary_search(target[i], data))