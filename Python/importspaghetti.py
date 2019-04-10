def hasCycle(v, visited, stack):
  visited[v] = True
  stack[v] = True

def main():
  n = int(input())
  files = input().split()
  deps = {}
  visitedtemp = {}
  for name in files:
    line = input().split()
    imports = int(line[1])
    deps[name] = []
    visitedtemp[name] = False
    for i in range(imports):
      linein = input()[7:]
      line = linein.split(", ")
      for dep in line:
        deps[name].append(dep)

  for name in deps:
    visited = dict(visitedtemp)
    q = [name]
    tree = {name: name}
    visited[name] = True
    print(deps)
    while q:
      curr = q.pop(0)
      for dep in deps[curr]:
        print(curr,dep)
        if visited[dep]:
          print(visited)
          print("CYCLE")
          return

        tree[dep] = curr
        visited[dep] = True
        q.append(dep)

  print("SHIP IT")


if __name__ == '__main__':
  main()
