import sys
from collections import deque
def main():
  lines = sys.stdin.read().splitlines()
  board = [x if x == '.' else int(x) for line in lines for x in line]
  tags = [{i for i in range(1,10)} if board[x] == '.' else {board[x]} for x in range(81)]
  path = [0, 1, 2, 9, 10, 11, 18, 19, 20]


  for i in range(81):
    if board[i] == '.':
      continue

    r, c = i//9, i%9
    R, C = r // 3, c // 3

    if len(tags[i]) == 1:
      crossout(board, tags, path, i, tags[i].pop())

  for i in range(81):
    if len(tags[i]) == 1:
      crossout(board, tags, path, i, tags[i].pop())
  
###
  changes = True 
  while changes:
    changes = False

    for i in range(81):
      if len(tags[i]) != 1:
        continue
      changes = True
      crossout(board, tags, path, i, tags[i].pop())

    for i in range(9):
      R, C = i//3, i%3 
      arr = [[] for _ in range(10)]
      for off in path:
        for num in tags[R*27+C*3+off]:
          arr[num].append(R*27+C*3+off)

      for j in range(1, 10):
        if len(arr[j]) == 1:
          changes = True
          board[arr[j][0]] = j
          crossout(board, tags, path, arr[j][0], j)


  if check(board,tags, path):
    for i in range(9):
      arr = []
      for j in range(9):
        arr.append(board[i*9+j])
      print(''.join(list(map(str, arr))))
  else:
    print('ERROR')

  


def check(board,tags, path):
  for i in range(81):
    if board[i] == '.':
      continue
    r, c = i//9, i%9
    R, C = r // 3, c // 3

    for j in range(9):
      if board[i] == board[j*9+c] and i != j*9+c:
        return False
      if board[i] == board[r*9+j] and i != r*9+j:
        return False

    for off in path:
      if board[R*27+C*3+off] == board[i] and R*27+C*3+off != i:
        return False


  for i in range(9):
    R, C = i//3, i%3 
    arr = [[] for _ in range(10)]
    for off in path:
      if board[R*27+C*3+off] != '.':
        arr[board[R*27+C*3+off]].append(R*27+C*3+off) 
      for num in tags[R*27+C*3+off]:
        arr[num].append(R*27+C*3+off)

    for j in range(1, 10):
      if len(arr[j]) == 0:
        return False
    

  return True

def crossout(board, tags, path, i, x):
  r, c = i//9, i%9
  R, C = r // 3, c // 3
  board[i] = x
  tags[i] = set()
  for j in range(9):
    tags[r*9+j].discard(x)
    if len(tags[r*9+j]) == 1:
      crossout(board, tags, path, r*9+j, tags[r*9+j].pop())
    tags[j*9+c].discard(x)
    if len(tags[j*9+c]) == 1:
      crossout(board, tags, path, j*9+c, tags[j*9+c].pop())
  for off in path:
    tags[R*27+C*3+off].discard(x)
    if len(tags[R*27+C*3+off]) == 1:
      crossout(board, tags, path, R*27+C*3+off, tags[R*27+C*3+off].pop())

if __name__ == '__main__':
  main()
