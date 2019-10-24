def main():
  R, C, K = map(int, input().split(' '))
  grid = [list(input()) for _ in range(R) ]

  biggest, row, col = 0, 0, 0
  for i in range(0, R-K+1):
    for j in range(0, C-K+1):
      curr = 0
      for k in range(i+1, i+K-1):
        for x in range(j+1, j+K-1):

          if grid[k][x] == '*':
            curr += 1
      if curr > biggest:
        biggest = max(curr, biggest)
        row, col = i, j


  for i in range(R):
    for j in range(C):
      if i == row or i == row + K-1:
        if j == col or j == col + K-1:
          grid[i][j] = "+"
        elif j > col and j < col + K-1:
          grid[i][j] = '-'
      elif j == col or j == col + K-1:
        if i > row and i < row + K-1:
          grid[i][j] = '|'


  print(biggest)
  for line in grid:
    print("".join(line))



if __name__ == '__main__':
  main()
