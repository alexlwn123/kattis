import sys
def main():
  INF = 9999999
  out = []
  line = sys.stdin.readline().strip().split(' ')
  while True:
    n, m, q = map(int, line)

    if n == m == q == 0:
      print('\n'.join(out))
      break

    graph = [[INF for _ in range(n)] for _ in range(n)]
    for _ in range(m):
      u, v, w = map(int, sys.stdin.readline().strip().split(' '))
      graph[u][v] = w

    for i in range(n):
      graph[i][i] = 0

    for k in range(n):
      for i in range(n):
        for j in range(n):
          graph[i][j] = min(graph[i][j], graph[i][k]+ graph[k][j])

    for _ in range(q):
      u, v = map(int, sys.stdin.readline().strip().split(' '))
      if graph[u][u] < 0 or graph[v][v] < 0:
        out.append('-Infinity')
      elif graph[u][v] == INF and graph[v][u]:
        out.append('Impossible')
      else:
        out.append(str(min(graph[u][v], graph[v][u])))

    out.append('')

    line = sys.stdin.readline().strip().split(' ')
    # for l in graph:
      # out.append(l)
if __name__ == '__main__':
  main()
