def main():
  n, x = map(int, input().split())
  items = sorted(list(map(int, input().split())))
  if n < 2 or items[0] + items[1] > x:
    print(1)
    return
  items = iter(items)
  count = 1

  first = next(items, None)
  second = next(items, None)
  while second is not None:
    if first + second <=x:
      count += 1
    else:
      break
    second, first = next(items,None), second
  print(count)


if __name__ == '__main__':
  main()
