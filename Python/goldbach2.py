import sys
from collections import deque
def main():
  lines = deque(list(map(int, sys.stdin.readlines())))
  primes = set()
  for i in range(2, 32000):
    yes = True
    for j in range(2, int(i ** .5) + 1):
      if i % j == 0:
        yes = False
        break
    if yes:
      primes.add(i)

  cases = lines.popleft()
  out = []
  for _ in range(cases):
    x = int(lines.popleft())
    solutions = []
    for i in range(x//2+1):
      if i in primes and x-i in primes:
        solutions.append("{}+{}".format(i, x-i))
    out.append('{} has {} representation(s)'.format(x, len(solutions)))
    out.append('\n'.join(solutions))
    out.append('')
  print('\n'.join(out))
if __name__ == '__main__':
  main()
