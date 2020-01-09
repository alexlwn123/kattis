# Fastest time using python3 on Kattis (1/8/2020)
import sys

def find(u, uf):
  if u == uf[u]:
    return u
  uf[u] = find(uf[u], uf)
  return uf[u]

def union(u, v, uf, size):
  uroot, vroot = find(u, uf), find(v, uf)
  if uroot == vroot:
    return

  if size[uroot] >= size[vroot]:
    uf[vroot] = uroot
    size[uroot] += size[vroot]
  else:
    uf[uroot] = vroot
    size[vroot] += size[uroot]

def main():
  lines = iter(sys.stdin.readlines())
  R, C = map(int, next(lines).strip().split())
  uf = [i for i in range(R * C)]
  size = [1] * R * C

  graph = [list(next(lines).strip()) for _ in range(R)]
  
  for i in range(R):
    for j in range(C):
      if j < C-1 and graph[i][j] == graph[i][j+1]:
        union(i*C+j, i*C+j+1, uf, size)
      if i < R-1 and graph[i][j] == graph[i+1][j]:
        union(i*C+j, (i+1)*C+j, uf, size)

  out = []
  for _ in range(int(next(lines).strip())):
    r1, c1, r2, c2 = [int(x)-1 for x in next(lines).strip().split()]
    if find(r1*C+c1, uf) == find(r2*C+c2, uf):
      out.append('decimal' if graph[r1][c1] == '1' else 'binary')
    else:
      out.append('neither')

  print('\n'.join(out))

if __name__ == '__main__':
  main()
