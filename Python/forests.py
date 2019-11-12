import sys
from collections import defaultdict
def find(uf, x):
  if uf[x] == x:
    return x
  uf[x] = find(uf, uf[x])
  return uf[x]

def union(uf, size, x, y):
  rootx, rooty = uf[x], uf[y]
  if rootx == rooty:
    return
  if size[rootx] >= size[rooty]:
    size[rootx] += size[rooty]
    uf[rooty] = rootx
  else:
    size[rooty] += size[rootx]
    uf[rootx] = rooty


def main():
  lines = [line.strip() for line in sys.stdin.readlines()]
  P, T = map(int, lines[0].split(' '))
  trees = [set() for _ in range(P+1)]
  uf = [i for i in range(P+1)]
  size = [1 for i in range(P+1)]
  for line in lines[1:]:
    u, v = map(int, line.split(' '))
    trees[u].add(v)

  for i in range(1, P+1):
    for j in range(1, P+1):
      if i == j:
        continue
      if trees[i] == trees[j]:
        union(uf, size, i, j)

  uniques = set()
  for i in range(1, P+1):
    uniques.add(find(uf, i))

  print(len(uniques))

if __name__ == '__main__':
  main()
