from heapq import heappush, heappop
from collections import defaultdict
def main():
  n, start, end = map(int, input().split())
  adj = defaultdict(list)
  edges = []
  dist = {}

  q = [(0, start)]
  heappush(q,(0,start))

  for u in range(n):
    line = list(map(int, input().split()))
    for v in range(n):
      if u != v:
        adj[u].append([v, line[v]])
  while len(dist) < n and q:
    cost, curr = heappop(q)
    if curr in dist and dist[curr] < cost:
      continue
    dist[curr] = cost
    for neighbor, val in adj[curr]:
      if neighbor in dist and dist[neighbor] <= cost + val:
        continue
      heappush(q, (cost+val, neighbor))

  print(dist[end])



if __name__ == '__main__':
  main()
