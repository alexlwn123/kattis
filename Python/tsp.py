import math
def main():
  n = int(input())
  arr = [tuple(map(float, x.split())) for x in range(n)]
  
  tour, used = [0]*n, [False]*n
  used[0] = True

  for i in range(1, n):
    best = -1
    for j in range(n):
      if not used[j] and (best = -1 or math.hypot(tour[i-1]


  


if __name__ == '__main__':
  main()
