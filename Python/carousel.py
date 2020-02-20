import sys
def main():
  lines = iter(list(map(int, line.split()) for line in sys.stdin.read().splitlines()))
  N, M = next(lines)
  while N != 0:
    A, B, m = 0, 99999, -1 
    for _ in range(N):
      a, b = next(lines)
      if a > M:
        continue
      if a/b > m:
        A, B, m = a, b, a/b
      elif a/b == m and a > A:
        A, B, m = a, b, a/b
    
    if m != -1:
      print(f'Buy {A} tickets for ${B}')
    else:
      print('No suitable tickets offered')


    N, M = next(lines)

if __name__ == '__main__':
  main()
