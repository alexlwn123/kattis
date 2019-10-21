from sys import stdin
def find(arr, x):
  if arr[x] == x:
    return x
  arr[x] = find(arr, arr[x])
  return arr[x]

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
  cases = int(stdin.readline().strip())
  for _ in range(cases):
    n = int(stdin.readline().strip())
    uf, size = {}, {}

    for _ in range(n):
      peops = stdin.readline().strip().split(' ')
      if not peops[0] in uf:
        uf[peops[0]] = peops[0]
        size[peops[0]] = 1

      if not peops[1] in uf:
        uf[peops[1]] = peops[1]
        size[peops[1]] = 1

      union(uf, size, peops[0], peops[1])
      print(size[find(uf, peops[0])])


if __name__ == '__main__':
  main()
