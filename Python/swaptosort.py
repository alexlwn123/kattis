import sys
def find(arr, u):
  if arr[u] == u:
    return arr[u]
  arr[u] = find(arr, arr[u])
  return arr[u]

def union(arr, size, u, v):
  uroot, vroot = find(arr, u), find(arr, v)
  if uroot == vroot:
    return

  if size[uroot] >= size[vroot]:
    arr[vroot] = uroot
    size[uroot] += size[vroot]
  else:
    arr[uroot] = vroot
    size[vroot] += size[uroot]


def main():
  lines = sys.stdin.readlines()
  n, k = map(int, lines[0].split(' '))
  del lines[0]
  uf = [i for i in range(n+1)]
  size = [1 for i in range(n+1)]

  for line in lines:
    u, v = map(int, line.strip().split(' '))
    union(uf, size, u, v)

  for i in range(1, n//2 +2):
    if find(uf, i) != find(uf, n-i+1):
      print('No')
      return

  print('Yes')

if __name__ == '__main__':
  main()
