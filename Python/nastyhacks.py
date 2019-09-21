n = int(input())
for _ in range(n):
  no, yee, cost = map(int, input().split())
  if yee - no > cost:
    print('advertise')
  elif yee - no < cost:
    print('do not advertise')
  else:
    print('does not matter')
