import heapq
def main():
  directions = [(0, -1), (0, 1), (1, 0), (-1, 0)]
  r, c = map(int, input().split())
  grid = [list(input().strip()) for _ in range(r)]
  flood = [[float('inf') for _ in x] for x in grid]
  walk =[[float('inf') for _ in x] for x in grid]
  visited = [[False for _ in range(c)] for _ in range(r)]

  q =[]
  for i in range(r):
    for j in range(c):
      if grid[i][j] == "*":
        heapq.heappush(q, (0, i, j))

  while q:
    curr, x, y = heapq.heappop(q)
    visited[x][y] = True
    if grid[x][y] == 'D' or grid[x][y] == 'X':
      continue
    flood[x][y] == curr

    for a, b in directions:
      x1, y1 = x+a, y+b
      if y1 < 0 or x1 < 0 or y1 >= c or x1 >= r or visited[x1][y1]:
        continue
      if flood[x1][y1] <= curr+1 or grid[x1][y1] == 'D' or grid[x1][y1] == 'X':
        continue
      if not visited[x1][y1]:
        heapq.heappush(q, (curr+1, x1, y1))

  q = []
  goal = None
  for i in range(r):
    for j in range(c):
      if grid[i][j] == 'S':
        heapq.heappush(q, (0, i, j))
      elif grid[i][j] == 'D':
        goal = (i, j)

  visited = [[False for _ in range(c)] for _ in range(r)]
  while q:
    curr, x, y = heapq.heappop(q)
    if visited[x][y]:
      continue
    visited[x][y] = True
    if walk[x][y] <= curr:
      continue
    walk[x][y] = curr
    if grid[x][y] == 'D':
      continue

    for a, b in directions:
      x1, y1 = x+a, y+b
      if y1 < 0 or x1 < 0 or y1 >= c or x1 >= r or visited[x1][y1]:
        continue
      if flood[x1][y1] <= curr+1 or grid[x1][y1] == 'X':
        continue
      heapq.heappush(q, (curr+1, x1, y1))

  ans = walk[goal[0]][goal[1]]

  if ans >= float('inf'):
    print('KAKTUS')
  else:
    print(ans)



if __name__ == '__main__':
  main()
