import sys
def find(uf, x):
  if uf[x] == x:
    return x
  uf[x] = find(uf, uf[x])
  return uf[x]

def union(uf, size, items, u, v):
  ur, vr = find(uf, u), find(uf, v)
  if ur == vr:
    return

  if size[ur] >= size[vr]:
    size[ur] += size[vr]
    uf[vr] = ur
    items[ur] += items[vr]
  else:
    size[vr] += size[ur]
    uf[ur] = vr
    items[vr] += items[ur]


def main():
  lines = [list(map(int, line.split())) for line in sys.stdin.read().splitlines()]
  uf = [i for i in range(300001)]
  size = [1]*300001
  items = [0]*300001
  out = []

  for a, b in lines[1:]:
    union(uf, size, items, a, b)
    r = find(uf, a)
    if items[r] == size[r]:
      out.append('SMECE')
    else:
      out.append('LADICA')
      items[r] += 1

  print('\n'.join(out))
    



if __name__ == '__main__':
  main()
