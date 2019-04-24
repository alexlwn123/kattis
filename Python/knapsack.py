import sys
from collections import deque
def main():
  out = deque()
  lines = deque(sys.stdin.readlines())
  while(lines):
    capacity, n = map(int, lines.popleft().split())
    values, weights = map(list, zip(*[map(int, lines.popleft().split()) for _ in range(n)]))

    memo = [[0]*(capacity+1) for _ in xrange(n+1)]

    for i in xrange(1, n+1):
      for w in xrange(1, capacity+1):
        if weights[i-1] > w:
          memo[i][w] = memo[i-1][w]
        else:
          memo[i][w] = max(memo[i-1][w-weights[i-1]]+values[i-1], memo[i-1][w])

    pos, bag = capacity, deque()

    for row in xrange(n, 0, -1):
      if memo[row][pos] != memo[row-1][pos]:
        bag.appendleft(str(row-1))
        pos -= weights[row-1]


    out.append(str(len(bag)))
    out.append(" ".join(bag))
  print "\n".join(out)

if __name__ == '__main__':
  main()
