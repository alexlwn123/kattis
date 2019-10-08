from collections import deque
def main():
  n, m, d = map(int, input().split())
  visited = {}
  graph = {}
  skep = {}
  toldfrom = {}
  for _ in range(n):
    line = input().split()
    skep[line[0]] = int(line[1])
    graph[line[0]] = []
    visited[line[0]] = 0
    toldfrom[line[0]] = set()
  for _ in range(m):
    line = input().split()
    graph[line[0]].append(line[1])
    graph[line[1]].append(line[0])

  q = deque()
  q.append(input())
  told = set([q[0]])
  while q:
    curr = q.popleft()
    if visited[curr] >= d:
      break
    for neighbor in graph[curr]:
      told.add(neighbor)
      skep[neighbor] -= 1
      visited[neighbor] = visited[curr] + 1
      if skep[neighbor] == 0:
        q.append(neighbor)

  total = 0
  print(len(told)-1)


if __name__ == '__main__':
  main()
