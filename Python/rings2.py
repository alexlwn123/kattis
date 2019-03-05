def main():
  height, width = map(int, input().split())
  grid = []
  visited = []
  tree = []
  MAX = 99999
  if height <= 0 or width <= 0:
    return
  for _ in range(height+2):
    grid.append([0 for _ in range(width+2)])
    visited.append([True for _ in range(width+2)])
  count = 0
  for i in range(1, height+1):
    line = list(input())
    for j in range(1, width+1):
      if line[j-1] == 'T':
        visited[i][j] = False
        tree.append([i,j])
        grid[i][j] = MAX
        count += 1
  directions = [[0,1], [1,0], [0,-1], [-1,0]]
  rings = 0
  changed = True

  while changed:
    changed = False
    rings += 1

    for i,j in tree:
      if visited[i][j]:
        continue
      for direc in directions:
        x, y = i + direc[0], j + direc[1]
        if grid[x][y] == rings-1:
          grid[i][j] = rings
          visited[i][j] = True
          changed = True
          break


  grid = grid[1:-1]
  for i in range(height):
    grid[i] = grid[i][1:-1]
    for j in range(width):
      if grid[i][j] == 0:
        grid[i][j] = '.'
      if rings >= 10:
        grid[i][j] = ('.' if grid[i][j] != '.' and grid[i][j] >= 10 else '..') + str(grid[i][j])
      else:
        grid[i][j] = '.' + str(grid[i][j])

  for i in range(len(grid)):
    grid[i] = "".join(grid[i])


  print('\n'.join(grid))


if __name__ == '__main__':
  main()

