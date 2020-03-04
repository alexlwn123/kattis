import sys
def main():
  N = int(sys.stdin.readline().strip())
  out = []
  for _ in range(N):
    n = int(sys.stdin.readline().strip())
    arr = list(map(int, sys.stdin.readline().strip().split()))

    i = 1
    count = 0
    for x in arr:
      if x == i:
        count += 1 
        i += 1
    out.append(str(len(arr)-count))

  print('\n'.join(out))



if __name__ == '__main__':
  main()
