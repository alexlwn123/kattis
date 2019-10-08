import sys
n = int(input())
yes = []
for _ in range(n):
  k = int(input())
  name = input()
  food = set()
  for i in range(k):
    food.add(input())
  if 'pea soup' in food and 'pancakes' in food:
    print(name)
    sys.exit()
print('Anywhere is fine I guess')
