tot = 0
n = float(input())
m = int(input())
for _ in range(m):
  l, w = map(float, input().split())
  tot += l * w * n
  print(tot)




