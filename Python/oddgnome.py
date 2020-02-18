N = int(input())
for _ in range(N):
  line = list(map(int, input().split()))
  n = line[0]
  arr = line[1:]
  for i in range(1, len(arr)-1):
    if (arr[i-1] > arr[i] and arr[i+1] > arr[i]) or (arr[i-1] < arr[i] and arr[i+1] < arr[i]): 
      if str([*arr[:i], *arr[i+1:]]) == str(sorted([*arr[:i], *arr[i+1:]])):
        print(i+1)
        break
       

