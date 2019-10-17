n, found = map(int, input().split(' '))
obs = set()
for _ in range(found):
  obs.add(int(input()))
for i in range(n):
  if i not in obs:
    print(i)
print(f'Mario got {len(obs)} of the dangerous obstacles.')
