import math
def main():
  b, k, g = map(int, input().split())
  G = k // g
  print(math.ceil((b-1) / G))


if __name__ == '__main__':
  main()
