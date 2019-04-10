def main():
  edges, nodes = map(int, input().split())
  while not edges == nodes == 0:
    edges, nodes = map(int, input().split())
    graph = {i:[] for i in range(nodes)}
    for i in range(nodes):
      line = input().split()
      u, v, w = int(line[0]), int(line[1]), float(line[2])
      graph[i]





if __name__ == '__main__':
  main()
