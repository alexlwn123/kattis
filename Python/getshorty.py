import sys
import heapq

class Node:

  def __init__(self, i):
    self.edges = {}
    self.ind = i
    self.visited = False
    self.score = 0

  def add(self, target, weight):

    if target not in self.edges:
      self.edges[target] = weight

    elif self.edges[target] < weight:
      self.edges[target] = weight

def main():
  while True:
    N, M = map(int, input().split())
    if N == M == 0:
      break

    
    nodes = [Node(i) for i in range(N)]
    for _ in range(M):
      line = input().split()
      u, v, w = int(line[0]), int(line[1]), float(line[2]) 
      nodes[u].add(v, w)
      nodes[v].add(u, w)

    q = [(-1, 0)]
    while q:
      uScore, u = heapq.heappop(q)
      uScore *= -1
      curr = nodes[u]
      if curr.visited:
        continue

      curr.score = uScore
      curr.visited = True

      if curr.ind == N-1:
        break
      
      for vi in curr.edges:
        v = nodes[vi]
        if v.visited:
          continue
        nScore = uScore*curr.edges[vi]
        heapq.heappush(q, (-nScore, v.ind))

    out = nodes[-1].score
    print("%1.4f"%out)

if __name__ == '__main__':
  main()
