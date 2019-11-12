from heapq import heappush, heappop, heapify
def main():
  R, C = map(int, input().split(' '))
  graph = []
  for _ in range(R):
    graph.append(list(map(int, input().split(' '))))

  visited = set()

  direct = [(0, 1), (0, -1), (1,0), (-1, 0)]
  moves = []
  for i in range(R):
    heappush(moves, (graph[i][0], i, 0))
    visited.add(i*C)

  small = -1
  while moves:
    depth, r, c = heappop(moves)
    small = max(small, depth)
    if c == C-1:
      print(small)
      return
    for x, y in direct:
      r1, c1 = r+x, c+y
      if r1 < 0 or c1 < 0 or r1 >= R or c1 >= C or r1*C+c1 in visited:
        continue
      visited.add(r1*C+c1)
      heappush(moves, (graph[r1][c1],r1, c1))



  print(-1)


if __name__ == '__main__':
  main()
