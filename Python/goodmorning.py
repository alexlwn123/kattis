poss = set()
def generate(grid,r,c,num):
  global poss
  if grid[r][c] == '.' or num > 200:
    return
  
  poss.add(num)

  if num != 0 or grid[r][c]!= 0:
    generate(grid, r, c, num*10+grid[r][c])

  if r < len(grid)-1:
    if grid[r+1][c] != '.':
      generate(grid, r+1, c, num*10+grid[r+1][c])
    generate(grid, r+1, c, num)
  
  if c < len(grid[0])-1:
    if grid[r][c+1] != '.':
      generate(grid, r, c+1, num*10+grid[r][c+1])
    generate(grid, r, c+1, num)

  
def main():
  grid = [['.']*3 for _ in range(4)]
  for i in range(3):
    for j in range(3):
      grid[i][j] = i*3+j+1
  grid[3][1] = 0
  generate(grid, 0, 0, 0)
  global poss
  T = int(input())
  nums = list(poss)
  for _ in range(T):
    n = int(input())
    print(min(nums, key=lambda x: abs(n-x)))




if __name__ == '__main__':
  main()
