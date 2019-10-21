import sys

lines = sys.stdin.readlines()

big = max([len(line.strip()) for line in lines])

total = 0
for line in lines[:-1]:
  total += (big - len(line.strip())) ** 2

print(total)
