x, y = int(input()), int(input())
if abs(y-x) == 180:
  print(180)
elif abs(y-x) < 180:
  print(y-x)
elif abs(y-x+360) < 180:
  print(y-x+360)
else:
  print(y-x-360)
