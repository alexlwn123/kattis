import sys
from collections import deque
def main():
  lines = sys.stdin.read().splitlines()
  N, H, L = map(int, lines[0].split())
  hor = list(map(int, lines[1].split()))
  neighbors = {i:[] for i in range(N)}
  HI = [999999 for i in range(N)]
  
  for u, v in list(tuple(map(int, line.split())) for line in lines[2:]):
    neighbors[u].append(v)
    neighbors[v].append(u)
    

  for h in hor:
    HI[h] = 0
  for start in hor:
    q = deque()
    q.append(start)

    while q:
      curr = q.popleft()
      for n in neighbors[curr]:
        HI[n] = min(HI[curr]+1, HI[n])



    
    


  



if __name__ == '__main__':
  main()
