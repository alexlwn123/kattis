def main():
  l, r = map(int, input().split())
  if l == r == 0:
    print('Not a moose')
  elif l == r:
    print('Even', l+r)
  else:
    print('Odd', 2*max(l, r))

if __name__ == '__main__':
  main()
