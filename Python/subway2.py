from collections import defaultdict
from heapq import heappush, heappop
import sys
from math import hypot

def main():
  WALK = 1
  BUS = 4
  
  fx, fy, tx, ty = map(int, sys.stdin.readline().strip().split())
  f, t = (fx, fy), (tx, ty)
  neighs = defaultdict(list)
  neighs[f].append((t, hypot(fx-tx, fy-ty)/WALK))
  neighs[t].append((f, hypot(fx-tx, fy-ty)/WALK))

  lists = [neighs]

  for line in sys.stdin.read().splitlines():
    neighbors = defaultdict(list)
    line = list(map(int, line.split()))[:-2]
    for i in range(0, len(line)-2, 2):
      u = (line[i], line[i+1])
      v = (line[i+2], line[i+3])
      neighbors[u].append((v, hypot(u[0]-v[0], u[1]-v[1])/BUS))
      neighbors[v].append((u, hypot(u[0]-v[0], u[1]-v[1])/BUS))
    lists.append(neighbors)


  neighbors = defaultdict(list)
  for d in lists:
    neighbors.update(d)

  for i in range(len(lists)):
    for j in range(i, len(lists)):
      if i == j:
        continue
      for x in lists[i].keys():
        for y in lists[j].keys():
          neighbors[x].append((y, hypot(x[0]-y[0], x[1]-y[1])/WALK))
          neighbors[y].append((x, hypot(x[0]-y[0], x[1]-y[1])/WALK))
          

  q, seen, distances = [(0, f)], set(), {f: 0}
  distances[t] = 9999999999999

  while q:

    dist, curr = heappop(q)
    if curr in seen or dist > distances[t]:
      continue
    seen.add(curr)
    
    for v, vc in neighbors[curr]:
      vc *= 6/1000
      if v not in seen and (v not in distances or dist + vc < distances[v]):
        distances[v] = dist + vc
        heappush(q, (distances[v], v))

  print(round(distances[t]))

  

if __name__ == '__main__':
  main()
