def main():
  x = int(input())
  for i in range(1,x+1):
    line = input().split(' ')[-1].split('/')
    n, d = int(line[0]), int(line[1])
    if d == 1:
      print('{} 1/{}'.format(i, n+1))
      continue
    depth = n//d
    n %= d
    d -= n
    n += d
    d += n*depth
    print('{} {}/{}'.format(i,n,d))

if __name__ == '__main__':
  main()
