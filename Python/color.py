def main():
  num, size, diff = map(int, input().split())
  if num == 1:
    print(1)
    return
  sox = sorted(list(map(int, input().split())))
  small, big = sox[0], sox[-1]

  tempmin, count, total = sox[0], 0, 1

  for sock in sox:
    if sock - tempmin > diff or count >= size:
      tempmin = sock
      total += 1
      count = 1
    else:
      count += 1

  print(total)

if __name__ == '__main__':
  main()
