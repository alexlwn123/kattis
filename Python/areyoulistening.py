import math
def main():
  cx, cy, n = map(int, input().split())
  arr = []
  dist = []
  for _ in range(n):    
    x, y, r = map(int, input().split())
    arr.append((x,y,r))
    dist.append((((cy - y) ** 2 + (cx - x) ** 2) ** 0.5)-r)

  dist.sort()
  print(math.floor(dist[2]))




if __name__ == '__main__':
  main()
