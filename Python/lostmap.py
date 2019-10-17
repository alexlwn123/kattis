import sys
from collections import deque
def find(uf, x):
  if uf[x] != x:
    uf[x] = find(uf, uf[x])
  return uf[x]

def union(uf, x, y):
  xroot, yroot = find(uf, x), find(uf, y)
  # print(uf)
  # print(xroot, yroot, x, y)
  if xroot == yroot:
    return
  uf[xroot] = yroot

def main():
  lines = deque(sys.stdin.readlines())
  n = int(lines.popleft().strip())

  adj = [list(map(int, lines.popleft().strip().split())) for _ in range(n)]
  for i in range(n):
    adj[i][i] = 10 ** 7 + 1

  mst = set()
  edges = set()

  for i in range(n):
    for j in range(i, n):
      if i == j:
        continue
      edges.add((i,j))

  sortEdges = sorted(edges, key=lambda x: adj[x[0]][x[1]])

  parents = [i for i in range(n)]
  for edge in sortEdges:
    u, v = edge
    if find(parents, u) == find(parents, v):
      continue
    union(parents, u, v)
    mst.add(edge)

  for e in mst:
    print(e[0]+1, e[1]+1)
if __name__ == '__main__':
  main()
