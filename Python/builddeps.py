from sys import stdin
from collections import defaultdict, deque
def markdated(name, below, dated):
  dated[name] = True

  for dep in below[name]:
    markdated(dep, below, dated)

def main():
  n = int(stdin.readline().strip())
  above = defaultdict(set)
  required = {}

  for _ in range(n):
    line = stdin.readline().strip().split(' ')
    line[0] = line[0][:-1]
    required[line[0]] = 0
    if len(line) == 1:
      continue

    for word in line[1:]:
      above[word].add(line[0])


  start = stdin.readline().strip()
  stack = deque([start])
  visited = set()

  while stack:
    curr = stack.pop()
    if curr in visited:
      continue
    visited.add(curr)
    for dep in above[curr]:
      required[dep] += 1
      if dep not in visited:
        stack.append(dep)

  stack = deque([start])
  while stack:
    curr = stack.pop()
    print(curr)
    for dep in above[curr]:
      required[dep] -= 1
      if required[dep] == 0:
        stack.append(dep)

if __name__ == '__main__':
  main()
