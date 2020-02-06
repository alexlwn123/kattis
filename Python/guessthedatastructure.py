import sys
from collections import deque
import heapq
def main():   
  lines = iter([x.strip() for x in sys.stdin.readlines()])
  out = []
  try:
    while True:
      N = int(next(lines))
      S,Q,H = deque(),deque(),[]
      s, q, h = [], [], []
      O = []

      good = True
      for _ in range(N):
        x, y = map(int, next(lines).split(' '))
        if not good:
          continue
        if x == 1:
          S.append(y)
          Q.append(y)
          heapq.heappush(H,  -y)
        else:
          if not S:
            good = False
            continue

          s.append(S.pop())
          q.append(Q.popleft())
          h.append(-heapq.heappop(H))
          O.append(y)
      a, b, c = str(s) == str(O), str(q) == str(O), str(h) == str(O)

      if a and not b and not c:
        out.append('stack')
      elif b and not a and not c:
        out.append('queue')
      elif c and not a and not b:
        out.append('priority queue')
      elif (not a and not b and not c) or not good:
        out.append('impossible')
      else:
        out.append('not sure')




  except StopIteration as Exception:
    print('\n'.join(out))
    return

if __name__ == '__main__':
  main()

