import sys
from collections import deque

def move(grid, i, j, n):
  temp = [x for x in grid]
  for r in range(3):
    for c in range(3):
      if c == j or r == i:
        temp[r*3+c] = (temp[r*3+c] + n + 4) % 4
  return tuple(temp)


def isSolved(grid):
  return str(grid) == str(tuple(0 for _ in range(9)))

def main():
  graph = []
  for line in sys.stdin:
    for x in line.split():
      graph.append(int(x))
  graph = tuple(graph)
  visited = {}
  visited[graph] = 0
  q = deque([graph])
  if isSolved(graph):
    print(0)
    return
  while q:
    curr = q.popleft()
    for index in range(9):

      row, col = index // 3, index % 3
      temp = move(curr, row, col, 1)
      if temp in visited:
        continue

      if isSolved(temp):
        print(visited[curr] + 1)
        return

      visited[temp] = visited[curr] +1
      q.append(temp)

  print(-1)




if __name__ == '__main__':
  main()
