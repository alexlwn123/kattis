g, s, c = map(int, input().split(" "))
x = 3 * g + 2 * s + c

if x >= 8:
  print('Province or Gold')
elif x >= 6:
  print('Duchy or Gold')
elif x >= 5:
  print('Duchy or Silver')
elif x >= 3:
  print('Estate or Silver')
elif x >= 2:
  print('Estate or Copper')
else:
  print('Copper')
