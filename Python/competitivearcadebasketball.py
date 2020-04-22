import sys
def main():
  lines = iter(sys.stdin.read().splitlines())
  n, p, m = map(int, next(lines).split())
  names = {} 
  won = set()
  no = True
  out = []
  for _ in range(n):
    names[next(lines)] = 0

  for _ in range(m):
    line = next(lines).split()
    names[line[0]] += int(line[1])
    if names[line[0]] >= p and line[0] not in won:
      won.add(line[0])
      out.append("{} wins!".format(line[0]))
      no = False

  if not out:
    print("No winner!")

  else:
    print('\n'.join(out))




if __name__ == '__main__':
  main()
