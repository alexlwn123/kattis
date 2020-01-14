def left(arr):
  temp = [0] * 4
  j = 0
  for i in range(4):
    if arr[i] != 0:
      temp[j] = arr[i]
      j+=1
  arr = temp

  for i in range(3):
    if arr[i] == arr[i+1]:
      arr[i] *= 2
      arr[i+1] = 0
    
  temp = [0] * 4
  j = 0
  for i in range(4):
    if arr[i] != 0:
      temp[j] = arr[i]
      j+=1
  arr = temp
  return arr

def main():
  grid = [list(map(int, input().split())) for _ in range(4)]
  direction = int(input())

  if direction == 0:
    for i in range(4):
      grid[i] = left(grid[i])

  if direction == 2:
    for i in range(4):
      grid[i] = left(grid[i][::-1])[::-1]

  if direction == 1:
    for i in range(4):
      arr = [grid[j][i] for j in range(4)]
      arr = left(arr)
      for j in range(4):
        grid[j][i] = arr[j]

  if direction == 3:
    for i in range(4):
      arr = [grid[j][i] for j in range(4)][::-1]
      arr = left(arr)[::-1]
      for j in range(4):
        grid[j][i] = arr[j]
    
  print('\n'.join([' '.join(list(map(str, x))) for x in grid]))

if __name__ == '__main__':
  main()
