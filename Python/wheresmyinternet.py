import sys
def find(uf, x):
  if uf[x] != x:
    uf[x] = find(uf, uf[x])
  return uf[x]

def union(uf, size, x, y):
  xroot, yroot = find(uf, x), find(uf, y)
  if xroot == yroot:
    return

  if size[xroot] < size[yroot]:
    xroot, yroot = yroot, xroot

  uf[yroot] = xroot
  size[xroot] += size[yroot]

def main():
  lines = sys.stdin.readlines()
  houses, cables = map(int, lines[0].split(' '))
  uf, size = [i for i in range(houses+1)], [1 for i in range(houses+1)]
  for i in range(1, cables+1):
    x, y = map(int, lines[i].split(' '))

    union(uf, size, x, y)

  yes = find(uf, 1)

  off = []
  for other in range(1,houses+1):
    if find(uf, other) != yes:
      off.append(other)

  if len(off) == 0:
    print('Connected')
  else:
    print('\n'.join(map(str,off)))

if __name__ == '__main__':
  main()
