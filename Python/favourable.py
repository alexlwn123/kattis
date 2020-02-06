import sys
from collections import deque, defaultdict
def main():
  lines = iter([x.strip() for x in sys.stdin.readlines()])
  T = int(next(lines))
  for _ in range(T):
    S = int(next(lines))
    P, C, V, Q = defaultdict(list), defaultdict(int) , defaultdict(int), deque()


    for i in range(S):
      line = next(lines).split()
      if len(line) == 2:
        Q.append(line[0])
        V[line[0]] += 1 if line[1] == 'favourably' else 0
      else:
        C[line[0]] += 3 
        for x in line[1:]:
          P[x].append(line[0])

    while True:
      x = Q.popleft()


      for p in P[x]:
        V[p] += V[x]
        C[p] -= 1
        if C[p] == 0:
          Q.append(p)

          
      if not Q:
        print(V[x])
        break
        
if __name__ == '__main__':
  main()
