import sys

if __name__ == '__main__':
  sys.stdin.readline()
  lines = sys.stdin.read().splitlines()
  print('\n'.join(reversed(lines)))
