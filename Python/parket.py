def main():
  r, b = map(int, input().split(' '))
  tot = r+b
  for i in range(r):
    for j in range(r):
      if 2*(i+j) - 4 != r:
        continue
      if i*j == tot:
        print(max(i, j), min(i,j))
        return

if __name__  == '__main__':
  main()
