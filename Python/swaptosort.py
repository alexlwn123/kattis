def find(u, arr):
  while arr[u] != u:
    n = arr[u]
    arr[u] = arr[arr[u]]
    u = n
  return arr[u]

def union(u, v, arr, size):
  upar, vpar = find(u, arr), find(v,arr)
  if upar == vpar:
    return
  if size[upar] > size[vpar]:
    arr[v] = upar
    size[upar] += size[vpar]
    size[vpar] = 0
  else:
    arr[u] = vpar
    size[vpar] += size[upar]
    size[upar] = 0

def main():
  n, k = map(int, input().split())
  arr = [i for i in range(n)]
  size = [1] * n
  for _ in range(k):
    u,v = map(int, input().split())
    union(u-1, v-1, arr, size)

  n-=1
  for i in range(n):
    find(i, arr)
  print(arr)
  for i in range(n//2):
    if arr[i] != arr[n-i]:

      print("No")
      return
  print("Yes")




if __name__ == '__main__':
  main()
