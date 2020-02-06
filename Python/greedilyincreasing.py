def main():
  n = int(input())
  arr = list(map(int, input().split()))
  curr = -1
  out = []
  for x in arr:
    if x > curr:
      out.append(x)
      curr = x

  print(len(out))
  print(' '.join([str(x) for x in out]))

if __name__ == '__main__':
  main()
