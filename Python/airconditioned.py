import sys
def main():
  n = int(sys.stdin.readline().strip())
  lines = sorted([tuple(map(int, x.split())) for x in sys.stdin.read().splitlines()], key=lambda l: (l[1],l[0]))

  c = 1
  curr = lines[0][1]
  for i in range(len(lines)):
    if lines[i][0] > curr:
      curr = max(curr, lines[i][1])
      c+=1
  print(c)
      



if __name__ == '__main__':
  main()
