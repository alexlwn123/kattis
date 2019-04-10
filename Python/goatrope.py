import math
def main():
  x, y, x1, y1, x2, y2 = map(int, input().split())

  if x1 <= x and x2 >= x:
    print(min(abs(y1-y), abs(y2-y)))
  elif y1 <= y and y2 >= y:
    print(min(abs(x1-x), abs(x2-x)))
  else:
    print(min(math.hypot(x1-x, y1-y), math.hypot(x2-x, y-y2), math.hypot(x1-x, y2-y), math.hypot(x2-x, y1-y)))

if __name__ == '__main__':
  main()
