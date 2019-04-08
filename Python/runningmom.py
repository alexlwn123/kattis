import collections
import sys
def dfs(been, curr, routes, safe):
  if curr in safe:
    return safe[curr]
  for other in routes[curr]:
    if other in been or dfs(been | {other}, other, routes, safe):
      safe[other] = True
      return True
  safe[curr] = False
  return False

def contains_loop(start, routes, safe):
  return dfs({start}, start, routes, safe)

def main():
  out = []
  safe = {}
  lines = [a.strip() for a in sys.stdin.readlines()]
  n = int(lines.pop(0))
  adj = collections.defaultdict(list)
  for _ in range(n):
    u, v = lines.pop(0).split()
    adj[u].append(v)
  for line in lines:
    good = contains_loop(line, adj, safe)
    out.append(line + (' safe' if good else ' trapped'))


  print('\n'.join(out))
  return

if __name__ == '__main__':
  main()
