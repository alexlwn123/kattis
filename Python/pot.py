n = int(input())
total = 0
for _ in range(n):
  line = input()
  total += int(line[:-1])**int(line[-1])
print(total)
