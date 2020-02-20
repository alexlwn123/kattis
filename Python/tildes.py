import sys
def find(uf, u):
  if uf[u] == u:
    return u    
  uf[u] = find(uf, uf[u])
  return uf[u]

def union(uf, size, u, v):
  ur, vr = find(uf, u), find(uf, v)
  if ur == vr:
    return
  
  if size[ur] >= size[vr]:
    size[ur] += size[vr]
    uf[vr] = ur
  else:
    size[vr] += size[ur]
    uf[ur] = vr


def main():
  N, Q = map(int, sys.stdin.readline().split())
  lines = [x.split() for x in sys.stdin.read().splitlines()]
  uf = [i for i in range(N+1)]
  size = [1] * (N+1) 
  out = []
  for line in lines:
    if line[0] == 't':
      union(uf, size, int(line[1]), int(line[2]))
    else:
      out.append(str(size[find(uf, int(line[1]))]))

  print('\n'.join(out))
  


if __name__ == '__main__':
  main()
