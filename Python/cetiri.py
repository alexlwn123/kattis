arr = sorted(list(map(int, input().split())))
d = 999999
for i in range(len(arr)-1):
  d = min(d, arr[i+1]-arr[i])

i = 1
while i < len(arr):
  if arr[i] - arr[i-1] != d:
    print(arr[i-1]+d)
    break
  i+=1
else:
  print(arr[-1]+d)




