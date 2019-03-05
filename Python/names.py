def main():
  line = input()
  small = size = len(line)

  for i in range(size):
    x, y, moves = i, size-1, i
    while x < y:
      if line[x] != line[y]:
        moves += 1
      x += 1
      y -= 1
    small = min(small, moves)
  print(small)

if __name__ == '__main__':
  main()
