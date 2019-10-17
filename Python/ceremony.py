def main():
  n = int(input())
  arr = sorted(list(map(int, input().split())))
  gonefloors = 0
  loc = 0
  i = 0
  while i < len(arr):
    if arr[0] - gonefloors > len(arr) - loc:
      break
    if arr[i] > gonefloors:
      gonefloors += 1
    i += 1

  print(gonefloors + len(arr) - i)


if __name__ == '__main__':
  main()

