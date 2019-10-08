from collections import deque
import sys
def main():
  lines = deque(sys.stdin.readlines())
  n, m, d = map(int, lines.popleft().strip().split())
  neighbors = {}
  skep = {}
  seen = {}
  for _ in range(n):
    line = lines.popleft().strip().split()
    skep[line[0]] = int(line[1])
    neighbors[line[0]] = []
    seen[line[0]] = False

  for _ in range(m):
    line = lines.popleft().strip().split()
    neighbors[line[0]].append(line[1])
    neighbors[line[1]].append(line[0])

  q = deque()
  q.append(lines.popleft().strip())
  told = set([q[0]])
  seen[q[0]] == True
  for _ in range(d):
    temp = []
    while q:
      curr = q.popleft()
      for neighbor in neighbors[curr]:
        if not seen[neighbor]:
          told.add(neighbor)
          skep[neighbor] -= 1
          if skep[neighbor] == 0:
            temp.append(neighbor)
    q = deque(temp)

  print(len(told)-1)

if __name__ == '__main__':
  main()
