import numpy as np
import sys
def main():
  lines = sys.stdin.readlines()

  n, k = map(int, lines.pop(0).split())
  arr = np.array([list(map(int, line.split())) for line in lines[:-1]], ndmin=2)
  count = 0
  print(arr, "\n")

  np.power(arr,2)

  print(arr, "\n")

if __name__ == '__main__':
  main()
