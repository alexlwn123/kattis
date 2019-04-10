def main():
  runspeed = 5.0
  shottime = 2.0
  shotdist = 50.0 ** 2

  x0, y0 = map(float, input().split())
  x1, y1 = map(float, input().split())
  n = int(input())
  nodes = [list(map(float,(input().split()))) for _ in range(n)]
  print(nodes)

  edges = []

  for i in range(len(nodes)):
    for j in range(len(nodes)):
      if i == j:
        continue
      u, v = nodes[i], nodes[j]





if __name__ == '__main__':
  main()
