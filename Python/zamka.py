low, high, target = int(input()), int(input()), int(input())

for i in range(low, high+1):
  if sum(list(map(int, list(str(i))))) == target:
    print(i)
    break

for i in range(high, low-1, -1):
  if sum(list(map(int, list(str(i))))) == target:
    print(i)
    break
