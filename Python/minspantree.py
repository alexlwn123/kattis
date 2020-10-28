def find(u, arr):
  if arr[u] == u:
    return u
  
  arr[u] = find(arr[u], arr)

  return arr[u]


def union(u, v, arr, size):
  x, y = find(u, arr), find(v, arr)
  if x == y:
    return

  if size[x] > size[y]:
    size[x] += size[y]
    arr[y] = x

  else:
    size[y] += size[x]
    arr[x] = y

def main():
  out = []
  n, m = map(int, input().split())
  while not (n == m == 0):
    uf = [i for i in range(n)]
    size = [1] * n
    edges = [list(map(int, input().split())) for _ in range(m)]

    if m < n-1:
      out.append('Impossible')
      n, m = map(int, input().split())
      continue

    edges.sort(key = lambda x: x[2])


    good = []
    cost = 0
    for edge in edges:
      if find(edge[0], uf) != find(edge[1], uf):
        union(edge[0], edge[1], uf, size)
        cost += edge[2]
        good.append(list(map(str, sorted((edge[0], edge[1])))))

    
    trees = set()
    for x in range(n):
      trees.add(find(x, uf))

    if len(trees) != 1:
      out.append('Impossible')
    else:
      out.append(str(cost))
      good.sort(key = lambda x: (x[0], x[1]))
      good = [' '.join(x) for x in good]
      out.extend(good)


    n, m = map(int, input().split())

  print('\n'.join(out))
  




if __name__ == '__main__':
  main()
