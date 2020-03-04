import sys
def main():
  lines = list(map(int, sys.stdin.read().splitlines()))[1:]
  balance = 100
  stox = 0
  by = True
  for i in range(len(lines)-1):
    if lines[i+1] > lines[i]:
      balance += min(balance//lines[i], 100000) * (lines[i+1]- lines[i])

  print(balance)

if __name__ == '__main__':
  main()
